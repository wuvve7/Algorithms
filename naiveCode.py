import PyPDF2
import os
import re

# 1- Reading and processing the document
def read_pdf_file(filePath):
    if filePath.lower().endswith(".pdf"):
        try:
            with open(filePath, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text() or ""
                if not text:
                    print("Warning: No text could be extracted from this PDF.")
                return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return None
    else:
        print("Error: The file is not a PDF.")
        return None

def naive_document_classification(document, categories):
    text = document.lower()
    words = re.findall(r'\b\w+\b', text)

    bestCategory = 'Uncategorized'
    maxCount = 0
    scores = {category: 0 for category in categories}

    # 3- Count keyword matches
    for word in words:
        for category, keywords in categories.items():
            if word in keywords:
                scores[category] += 1

    # 4- Determine the best category
    for category, score in scores.items():
        if score > maxCount:
            maxCount = score
            bestCategory = category

    # 5- Return the result
    return bestCategory

# Categories and keywords
categories = {
    "Technology": ["computer", "software", "ai", "machine learning", "programming", "cloud computing", "iot", "data science", "cybersecurity", "virtual reality", "blockchain", "networking", "app development", "robotics", "C++", "Python", "Code", "Java"],
    "Sports": ["football", "basketball", "tennis", "player", "coach", "team", "training", "stadium", "referee", "match", "athlete", "tournament", "swimming", "cricket"],
    "Health": ["medicine", "doctor", "hospital", "treatment", "nutrition", "exercise", "mental health", "disease", "surgery", "therapy", "wellness", "diet", "healthcare", "vaccination", "nurse", "patient"],
    "Physics": ["Force", "Energy", "Matter", "Mass", "Velocity", "Acceleration", "Rate", "Motion", "Gravity", "Resistance","Pressure", "Dynamics", "Mechanics", "Electricity", "Magnetism", "Wave", "Heat", "Time", "Vacuum","sun", "stars", "alpha", "beta", "Frequency","Charge", "Relativity", "Momentum", "Thermodynamics", "Field", "Pulse", "Oscillator", "Reflection", "Spectrum","Quantum", "Wavefunction", "Schrodinger", "Heisenberg", "Superposition", "Entanglement", "Quantum mechanics","Photon", "Particle", "Atom", "Electromagnetic", "Radiation", "Optics", "Refraction", "Reflection","Diffraction", "Interference", "Polarization", "Electrostatics", "Magnetostatics", "Maxwell's equations", "Coulomb's law","Ampère's law", "Faraday's law", "Magnetic field", "Electric field", "Gravitational waves", "Black holes","Dark matter", "Dark energy", "String theory", "Higgs boson", "Standard model", "Cosmology", "Astrophysics","Particle physics", "High-energy physics", "Nuclear physics", "Plasma physics", "Optoelectronics","Semiconductor","Cryogenics", "Thermal expansion", "Viscosity", "Bose-Einstein condensate", "Laser", "Radiation pressure","Laser optics","Thermodynamic equilibrium", "Entropy", "Enthalpy", "Boltzmann constant", "Laws of thermodynamics","Entropy change","Adiabatic process", "Heat capacity", "Isothermal", "Carnot cycle", "Thermal conductivity","Blackbody radiation","Bohr model", "Fermionic", "Bosonic", "Wave-particle duality", "Einstein's theory", "Nuclear decay", "Quarks","Leptons", "Quark-gluon plasma", "Accelerators", "CERN", "LIGO", "CMB (Cosmic Microwave Background)","Redshift","Big Bang", "Einstein-Rosen bridge", "Schwarzschild radius", "Gravitational lensing"],
    "Chemistry": ["Chemistry", "Compound", "Mass","Enthalpy","London Forces", "melting" "Electrodes", "boiling point", "Molecular", "Metallic", "Ionic", "crystalline solid" "Combined Gas Law", "Viscosity", "Hess’ Law", "Methane","empirical", "molecular", "homogeneous", "concentration", "Molarity", "Molality", "Charles Law","Oxidation","Reduction","Electrodes" "Enthalpy", "Avogadro’s Law","Melting", "Freezing", "Sublimation", "Calorimetry", "Element", "Molecule","Substance", "Ion", "Oxidation", "Atom", "Molecular", "Reduction", "Solution", "Density", "Liquid", "Solid", "Metals","Non-metals","Metalloids", "Oxidation", "Reduction", "Acids", "Reactants", "Mole", "Alkanes", "Alkenes", "Alkynes", "Esters", "Amines","Crystalline","Periodic table", "Electronegativity", "Bonding", "Covalent", "Ionic", "Polar", "Non-polar", "Hydrogen bonding","Acid-base", "pH", "Titration", "Catalysis", "Isomerism", "Solubility", "Chemical reaction", "Reactivity","Thermodynamics","Heat of reaction", "Bond energy", "Le Chatelier's principle", "Kinetics", "Rate law", "Activation energy","Thermal decomposition","Stoichiometry", "Atomic mass", "Molarity", "Equilibrium", "Redox", "Electrochemistry", "Voltaic cells","Electrolysis","Anode", "Cathode", "Buffer", "Biochemistry","Enzyme","DNA", "RNA", "Amino acids","Analytical chemistry","Spectroscopy", "Mass spectrometry", "Electrochemical analysis", "Nanomaterials", "Nanochemistry", "Organic reactions","Photochemistry","Solvent", "Solvation", "Acid-base titration", "Coordination complex", "Ligands", "Transition metals","Organometallic","Polymer chemistry", "Aliphatic compounds", "Heterocyclic", "Catalysts", "Green chemistry","Pharmaceutical chemistry","Environmental chemistry", "Forensic chemistry"],
    "Mathematics": ["algebra", "geometry", "calculus", "statistics", "probability", "trigonometry", "integrals", "derivatives", "functions", "logic", "combinatorics"],
    "History": ["ancient", "medieval", "modern", "war", "civilization", "revolution", "empire", "kingdom", "timeline", "archaeology", "dynasty", "battle", "colonialism", "history"],
    "Economics": ["market", "supply", "demand", "currency", "inflation", "gdp", "unemployment", "recession", "taxation", "trade", "business", "investment", "capital"],
    "Languages": ["english", "spanish", "french", "grammar", "vocabulary", "phonetics", "pronunciation", "translation", "conjugation", "linguistics", "dialects"],
    "Psychology": ["mind", "behavior", "cognition", "emotion", "therapy", "counseling", "neuroscience", "memory", "personality"]
}

# 6- Enter the file path from the user
filePath = input("Enter your pdf file path: ")

# 7- Call the function to read the text
document = read_pdf_file(filePath)
if document:
    # 8- Classify the document using the function
    result = naive_document_classification(document, categories)
    print("\nPredicted category: ", result)
else:
    print("Could not read the document.")
