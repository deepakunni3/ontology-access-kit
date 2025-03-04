import os
import pprint
from pathlib import Path

ROOT = os.path.abspath(os.path.dirname(__file__))
INPUT_DIR = Path(ROOT) / 'input'
OUTPUT_DIR = Path(ROOT) / 'output'
SCHEMA_DIR = Path(ROOT) / '../src/linkml'
EXTERNAL_DB_DIR = Path(ROOT) / '../db'   ## for integration tests: optional

def output_path(fn: str) -> str:
    return str(Path(OUTPUT_DIR) / fn)


DIGIT = 'UBERON:0002544'
VACUOLE = 'GO:0005773'
CYTOPLASM = 'GO:0005737'
HUMAN = 'NCBITaxon:9606'
MAMMALIA = 'NCBITaxon:40674'
NEURON = 'CL:0000540'
CELLULAR_COMPONENT = 'GO:0005575'
CELLULAR_ANATOMICAL_ENTITY = 'GO:0110165'
CELL = 'CL:0000000'
SHAPE = 'PATO:0000052'
NUCLEATED = 'PATO:0002505'
PHOTORECEPTOR_OUTER_SEGMENT = 'GO:0001750'
CATALYTIC_ACTIVITY = 'GO:0003824'

CHEBI_NUCLEUS = 'CHEBI:33252'
NUCLEUS = 'GO:0005634'
NUCLEAR_ENVELOPE = 'GO:0005635'
THYLAKOID = 'GO:0009579'
ATOM = 'CHEBI:33250'
INTERNEURON = 'CL:0000099'
BACTERIA = 'NCBITaxon:2'
EUKARYOTA = 'NCBITaxon:2759'
FUNGI = 'NCBITaxon:4751'
CELLULAR_ORGANISMS = 'NCBITaxon:131567'
PLANTS_OR_CYANOBACTERIA = 'NCBITaxon_Union:0000002'
FUNGI_OR_DICTYOSTELIUM = 'NCBITaxon_Union:0000022'
FUNGI_OR_BACTERIA = 'NCBITaxon_Union:0000020'

BIOLOGICAL_PROCESS = 'GO:0008150'
NEGEG_PHOSPH = 'GO:0042326'
DICTYOSTELIUM = 'NCBITaxon:5782'
DICTYOSTELIUM_DISCOIDEUM = 'NCBITaxon:44689'
NUCLEAR_MEMBRANE = 'GO:0031965'
PHOTOSYNTHETIC_MEMBRANE = 'GO:0034357'
SOROCARP_STALK_DEVELOPMENT = 'GO:0031150'

INTRACELLULAR = 'GO:0005622'

TISSUE = 'UBERON:0000479'

FAKE_ID = 'FAKE:001'
FAKE_PREDICATE = 'FAKEPRED:001'