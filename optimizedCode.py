import PyPDF2
import os
import re

# 1. Reading the file and processing it
def read_pdf_file(filePath):
    if filePath.lower().endswith(".pdf"):  # Check if the file is a PDF
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
            print(f"Error reading the file: {e}")
            return None
    else:
        print("Error: The file is not a PDF.")
        return None

# 2. Processing the text and splitting it into words
def preprocess_and_split(text):
    text = text.lower()
    return re.findall(r'\b\w+\b', text)  # Use regular expression

# 3. Building the inverted index
def build_inverted_index(categories):
    inverted_index = {}
    for category, keywords in categories.items():  # Iterate over categories and their keywords
        for keyword in keywords:
            if keyword not in inverted_index:
                inverted_index[keyword] = []
            inverted_index[keyword].append(category)
    return inverted_index

# 4. Classifying the document using the inverted index
def optimized_document_classification(document, categories):
    words = preprocess_and_split(document)

    inverted_index = build_inverted_index(categories)

    match_count = {}
    for word in words:
        if word in inverted_index:
            for category in inverted_index[word]:
                if category not in match_count:
                    match_count[category] = 0
                match_count[category] += 1

    # Finding the category with the highest match count
    best_category = "Uncategorized"
    max_count = 0
    for category, count in match_count.items():
        if count > max_count:
            max_count = count
            best_category = category

    # Return the best category or "Uncategorized" if no matches
    return best_category

# Categories and their keywords
categories = {
    "Technology": ["computer", "software", "ai", "machine learning", "programming", "cloud computing", "iot", "data science", "cybersecurity", "virtual reality", "blockchain", "networking", "app development", "robotics", "C++", "Python", "Code", "Java"],
    "Sports": ["football", "basketball", "tennis", "player", "coach", "team", "training", "stadium", "referee", "match", "athlete", "tournament", "swimming", "cricket"],
    "Health": ["medicine", "doctor", "hospital", "treatment", "nutrition", "exercise", "mental health", "disease", "surgery", "therapy", "wellness", "diet", "healthcare", "vaccination", "nurse", "patient"],
    "Physics": ["force", "energy", "matter", "mass", "velocity", "acceleration", "rate", "motion", "gravity", "resistance","pressure", "dynamics", "mechanics", "electricity", "magnetism", "wave", "heat", "time", "vacuum","sun", "stars", "alpha", "beta", "frequency","charge", "relativity", "momentum", "thermodynamics", "field", "pulse", "oscillator", "reflection", "spectrum","quantum", "wavefunction", "schrodinger", "heisenberg", "superposition", "entanglement", "quantum mechanics","photon", "particle", "atom", "electromagnetic", "radiation", "optics", "refraction", "reflection","diffraction", "interference", "polarization", "electrostatics", "magnetostatics", "maxwell's equations", "coulomb's law","ampère's law", "faraday's law", "magnetic field", "electric field", "gravitational waves", "black holes","dark matter", "dark energy", "string theory", "higgs boson", "standard model", "cosmology", "astrophysics","particle physics", "high-energy physics", "nuclear physics", "plasma physics", "optoelectronics","semiconductor","cryogenics", "thermal expansion", "viscosity", "bose-einstein condensate", "laser", "radiation pressure","laser optics","thermodynamic equilibrium", "entropy", "enthalpy", "boltzmann constant", "laws of thermodynamics","entropy change","adiabatic process", "heat capacity", "isothermal", "carnot cycle", "thermal conductivity","blackbody radiation","bohr model", "fermionic", "bosonic", "wave-particle duality", "einstein's theory", "nuclear decay", "quarks","leptons", "quark-gluon plasma", "accelerators", "cern", "ligo", "cmb (cosmic microwave background)","redshift","big bang", "einstein-rosen bridge", "schwarzschild radius", "gravitational lensing"],
    "Chemistry": ["chemistry", "compound", "mass","enthalpy","london forces", "melting" "electrodes", "boiling point", "molecular", "metallic", "ionic", "crystalline solid" "combined gas law", "Viscosity", "hess’ law", "mthane","empirical", "molecular", "homogeneous", "concentration", "molarity", "molality", "charles Law","oxidation","reduction","electrodes", "Avogadro’s law","Melting", "freezing", "sublimation", "calorimetry", "element", "molecule","substance", "Ion", "Oxidation", "atom", "molecular", "reduction", "solution", "density", "liquid", "solid", "metals","non-metals","metalloids", "oxidation", "reduction", "acids", "reactants", "mole", "alkanes", "alkenes", "alkynes", "esters", "amines","crystalline","periodic table", "electronegativity", "bonding", "covalent", "ionic", "polar", "non-polar", "hydrogen bonding","acid-base", "pH", "Titration", "catalysis", "isomerism", "solubility", "chemical reaction", "reactivity","thermodynamics","heat of reaction", "bond energy", "le chatelier's principle", "kinetics", "rate law", "activation energy","thermal decomposition","stoichiometry", "atomic mass", "molarity", "equilibrium", "redox", "electrochemistry", "voltaic cells","electrolysis","anode", "cathode", "buffer", "biochemistry","enzyme","dna", "rna", "amino acids","analytical chemistry","spectroscopy", "mass spectrometry", "electrochemical analysis", "nanomaterials", "nanochemistry", "organic reactions","photochemistry","solvent", "solvation", "acid-base titration", "coordination complex", "ligands", "transition metals","organometallic","polymer chemistry", "aliphatic compounds", "heterocyclic", "catalysts", "green chemistry","pharmaceutical chemistry","environmental chemistry", "forensic chemistry"],
    "Mathematics": ["algebra", "geometry", "calculus", "statistics", "probability", "trigonometry", "integrals", "derivatives", "functions", "logic", "combinatorics"],
    "History": ["ancient", "medieval", "modern", "war", "civilization", "revolution", "empire", "kingdom", "timeline", "archaeology", "dynasty", "battle", "colonialism", "history"],
    "Economics": ["market", "supply", "demand", "currency", "inflation", "gdp", "unemployment", "recession", "taxation", "trade", "business", "investment", "capital"],
    "Languages": ["english", "spanish", "french", "grammar", "vocabulary", "phonetics", "pronunciation", "translation", "conjugation", "linguistics", "dialects"],
    "Psychology": ["mind", "behavior", "cognition", "emotion", "therapy", "counseling", "neuroscience", "memory", "personality"]
}

# 8. Taking file path input from the user
filePath = input("Enter your pdf file path: ")

# 9. Reading the document
document = read_pdf_file(filePath)

if document:
    # 10. Classifying the document using the inverted index
    result = optimized_document_classification(document, categories)
    print("\nPredicted category: ", result)
else:
    print("Could not read the document.")
