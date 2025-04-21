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
    "Physics": ["force", "energy", "matter", "mass", "velocity", "acceleration", "rate", "motion", "gravity", "resistance","pressure", "dynamics", "mechanics", "electricity", "magnetism", "wave", "heat", "time", "vacuum","sun", "stars", "alpha", "beta", "frequency","charge", "relativity", "momentum", "thermodynamics", "field", "pulse", "oscillator", "reflection", "spectrum","quantum", "wavefunction", "schrodinger", "heisenberg", "superposition", "entanglement", "quantum mechanics","photon", "particle", "atom", "electromagnetic", "radiation", "optics", "refraction", "reflection","diffraction", "interference", "polarization", "electrostatics", "magnetostatics", "maxwell's equations", "coulomb's law","ampère's law", "faraday's law", "magnetic field", "electric field", "gravitational waves", "black holes","dark matter", "dark energy", "string theory", "higgs boson", "standard model", "cosmology", "astrophysics","particle physics", "high-energy physics", "nuclear physics", "plasma physics", "optoelectronics","semiconductor","cryogenics", "thermal expansion", "viscosity", "bose-Einstein condensate", "laser", "radiation pressure","laser optics","thermodynamic equilibrium", "entropy", "enthalpy", "boltzmann constant", "laws of thermodynamics","entropy change","adiabatic process", "heat capacity", "isothermal", "carnot cycle", "thermal conductivity","blackbody radiation","bohr model", "fermionic", "bosonic", "wave-particle duality", "einstein's theory", "nuclear decay", "quarks","leptons", "quark-gluon plasma", "accelerators", "cern", "ligo", "cmb (cosmic microwave background)","redshift","big bang", "einstein-Rosen bridge", "schwarzschild radius", "gravitational lensing"],
    "Chemistry": ["chemistry", "compound", "mass","enthalpy","london forces", "melting" "electrodes", "boiling point", "molecular", "metallic", "crystalline solid" "combined gas law", "viscosity", "hess’ law", "methane","empirical", "molecular", "homogeneous", "concentration", "molality", "charles Law","reduction","electrodes" "enthalpy", "avogadro’s Law","melting", "freezing", "sublimation", "calorimetry", "element", "molecule","substance", "ion", "atom", "molecular", "reduction", "solution", "density", "liquid", "solid", "metals","non-metals","metalloids", "oxidation", "reduction", "acids", "reactants", "mole", "alkanes", "alkenes", "alkynes", "esters", "amines","crystalline","periodic table", "electronegativity", "bonding", "covalent", "ionic", "polar", "non-polar", "hydrogen bonding","acid-base", "pH", "titration", "catalysis", "isomerism", "solubility", "chemical reaction", "reactivity","thermodynamics","heat of reaction", "bond energy", "le chatelier's principle", "kinetics", "rate law", "activation energy","thermal decomposition","stoichiometry", "atomic mass", "molarity", "equilibrium", "redox", "electrochemistry", "voltaic cells","electrolysis","anode", "cathode", "buffer", "biochemistry","enzyme","dna", "rna", "amino acids","analytical chemistry","spectroscopy", "mass spectrometry", "electrochemical analysis", "nanomaterials", "nanochemistry", "organic reactions","photochemistry","solvent", "solvation", "acid-base titration", "coordination complex", "ligands", "transition metals","organometallic","polymer chemistry", "aliphatic compounds", "heterocyclic", "catalysts", "green chemistry","pharmaceutical chemistry","environmental chemistry", "forensic chemistry"],
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
