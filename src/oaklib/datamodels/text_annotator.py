# Auto generated from text_annotator.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-05-06T18:20:18
# Schema: text-annotator
#
# id: https://w3id.org/linkml/text_annotator
# description: A datamodel for representing the results of textual named entity recognition annotation results
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ANN = CurieNamespace('ann', 'https://w3id.org/linkml/text_annotator/')
BPA = CurieNamespace('bpa', 'https://bioportal.bioontology.org/annotator/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SH = CurieNamespace('sh', 'https://w3id.org/shacl/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SSSOM = CurieNamespace('sssom', 'http://w3id.org/sssom/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ANN


# Types
class Position(Integer):
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "Position"
    type_model_uri = ANN.Position


# Class references
class TextualElementId(URIorCURIE):
    pass


@dataclass
class TextAnnotationResultSet(YAMLRoot):
    """
    A collection of annotation results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANN.TextAnnotationResultSet
    class_class_curie: ClassVar[str] = "ann:TextAnnotationResultSet"
    class_name: ClassVar[str] = "TextAnnotationResultSet"
    class_model_uri: ClassVar[URIRef] = ANN.TextAnnotationResultSet

    annotations: Optional[Union[Union[dict, "TextAnnotation"], List[Union[dict, "TextAnnotation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.annotations, list):
            self.annotations = [self.annotations] if self.annotations is not None else []
        self.annotations = [v if isinstance(v, TextAnnotation) else TextAnnotation(**as_dict(v)) for v in self.annotations]

        super().__post_init__(**kwargs)


@dataclass
class TextualElement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANN.TextualElement
    class_class_curie: ClassVar[str] = "ann:TextualElement"
    class_name: ClassVar[str] = "TextualElement"
    class_model_uri: ClassVar[URIRef] = ANN.TextualElement

    id: Union[str, TextualElementId] = None
    text: Optional[str] = None
    source_text: Optional[str] = None
    parent_document: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TextualElementId):
            self.id = TextualElementId(self.id)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.source_text is not None and not isinstance(self.source_text, str):
            self.source_text = str(self.source_text)

        if self.parent_document is not None and not isinstance(self.parent_document, URIorCURIE):
            self.parent_document = URIorCURIE(self.parent_document)

        super().__post_init__(**kwargs)


@dataclass
class HasSpan(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANN.HasSpan
    class_class_curie: ClassVar[str] = "ann:HasSpan"
    class_name: ClassVar[str] = "HasSpan"
    class_model_uri: ClassVar[URIRef] = ANN.HasSpan

    subject_start: Optional[Union[int, Position]] = None
    subject_end: Optional[Union[int, Position]] = None
    subject_label: Optional[str] = None
    subject_source: Optional[str] = None
    subject_text_id: Optional[Union[str, TextualElementId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_start is not None and not isinstance(self.subject_start, Position):
            self.subject_start = Position(self.subject_start)

        if self.subject_end is not None and not isinstance(self.subject_end, Position):
            self.subject_end = Position(self.subject_end)

        if self.subject_label is not None and not isinstance(self.subject_label, str):
            self.subject_label = str(self.subject_label)

        if self.subject_source is not None and not isinstance(self.subject_source, str):
            self.subject_source = str(self.subject_source)

        if self.subject_text_id is not None and not isinstance(self.subject_text_id, TextualElementId):
            self.subject_text_id = TextualElementId(self.subject_text_id)

        super().__post_init__(**kwargs)


@dataclass
class TextAnnotation(YAMLRoot):
    """
    An individual text annotation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANN.TextAnnotation
    class_class_curie: ClassVar[str] = "ann:TextAnnotation"
    class_name: ClassVar[str] = "TextAnnotation"
    class_model_uri: ClassVar[URIRef] = ANN.TextAnnotation

    predicate_id: Optional[str] = None
    object_id: Optional[str] = None
    object_label: Optional[str] = None
    object_source: Optional[str] = None
    confidence: Optional[float] = None
    match_string: Optional[str] = None
    is_longest_match: Optional[Union[bool, Bool]] = None
    matches_whole_text: Optional[Union[bool, Bool]] = None
    match_type: Optional[str] = None
    info: Optional[str] = None
    subject_start: Optional[Union[int, Position]] = None
    subject_end: Optional[Union[int, Position]] = None
    subject_label: Optional[str] = None
    subject_source: Optional[str] = None
    subject_text_id: Optional[Union[str, TextualElementId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.predicate_id is not None and not isinstance(self.predicate_id, str):
            self.predicate_id = str(self.predicate_id)

        if self.object_id is not None and not isinstance(self.object_id, str):
            self.object_id = str(self.object_id)

        if self.object_label is not None and not isinstance(self.object_label, str):
            self.object_label = str(self.object_label)

        if self.object_source is not None and not isinstance(self.object_source, str):
            self.object_source = str(self.object_source)

        if self.confidence is not None and not isinstance(self.confidence, float):
            self.confidence = float(self.confidence)

        if self.match_string is not None and not isinstance(self.match_string, str):
            self.match_string = str(self.match_string)

        if self.is_longest_match is not None and not isinstance(self.is_longest_match, Bool):
            self.is_longest_match = Bool(self.is_longest_match)

        if self.matches_whole_text is not None and not isinstance(self.matches_whole_text, Bool):
            self.matches_whole_text = Bool(self.matches_whole_text)

        if self.match_type is not None and not isinstance(self.match_type, str):
            self.match_type = str(self.match_type)

        if self.info is not None and not isinstance(self.info, str):
            self.info = str(self.info)

        if self.subject_start is not None and not isinstance(self.subject_start, Position):
            self.subject_start = Position(self.subject_start)

        if self.subject_end is not None and not isinstance(self.subject_end, Position):
            self.subject_end = Position(self.subject_end)

        if self.subject_label is not None and not isinstance(self.subject_label, str):
            self.subject_label = str(self.subject_label)

        if self.subject_source is not None and not isinstance(self.subject_source, str):
            self.subject_source = str(self.subject_source)

        if self.subject_text_id is not None and not isinstance(self.subject_text_id, TextualElementId):
            self.subject_text_id = TextualElementId(self.subject_text_id)

        super().__post_init__(**kwargs)


# Enumerations
class TransformationType(EnumDefinitionImpl):
    """
    A controlled datamodels of the types of transformation that can be applied to
    """
    Stemming = PermissibleValue(text="Stemming",
                                       description="Removal of the last few characters of a word to yield a stem term for each word in the term")
    Lemmatization = PermissibleValue(text="Lemmatization",
                                                 description="Contextual reduction of a word to its base form for each word in the term")
    WordOrderNormalization = PermissibleValue(text="WordOrderNormalization",
                                                                   description="reorder words in the term to a standard order such that comparisons are order-independent")
    Depluralization = PermissibleValue(text="Depluralization",
                                                     description="Transform plural form to singular form for each word in a term")
    CaseNormalization = PermissibleValue(text="CaseNormalization",
                                                         description="Transform term to a standard case, typically lowercase")
    WhitespaceNormalization = PermissibleValue(text="WhitespaceNormalization",
                                                                     description="Trim whitespace, condense whitespace runs, and transform all non-space whitespace to spaces")
    TermExpanson = PermissibleValue(text="TermExpanson",
                                               description="Expand terms using a dictionary")

    _defn = EnumDefinition(
        name="TransformationType",
        description="A controlled datamodels of the types of transformation that can be applied to",
    )

# Slots
class slots:
    pass

slots.textAnnotationResultSet__annotations = Slot(uri=ANN.annotations, name="textAnnotationResultSet__annotations", curie=ANN.curie('annotations'),
                   model_uri=ANN.textAnnotationResultSet__annotations, domain=None, range=Optional[Union[Union[dict, TextAnnotation], List[Union[dict, TextAnnotation]]]])

slots.textualElement__id = Slot(uri=ANN.id, name="textualElement__id", curie=ANN.curie('id'),
                   model_uri=ANN.textualElement__id, domain=None, range=URIRef)

slots.textualElement__text = Slot(uri=ANN.text, name="textualElement__text", curie=ANN.curie('text'),
                   model_uri=ANN.textualElement__text, domain=None, range=Optional[str])

slots.textualElement__source_text = Slot(uri=ANN.source_text, name="textualElement__source_text", curie=ANN.curie('source_text'),
                   model_uri=ANN.textualElement__source_text, domain=None, range=Optional[str])

slots.textualElement__parent_document = Slot(uri=ANN.parent_document, name="textualElement__parent_document", curie=ANN.curie('parent_document'),
                   model_uri=ANN.textualElement__parent_document, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.hasSpan__subject_start = Slot(uri=ANN.subject_start, name="hasSpan__subject_start", curie=ANN.curie('subject_start'),
                   model_uri=ANN.hasSpan__subject_start, domain=None, range=Optional[Union[int, Position]])

slots.hasSpan__subject_end = Slot(uri=ANN.subject_end, name="hasSpan__subject_end", curie=ANN.curie('subject_end'),
                   model_uri=ANN.hasSpan__subject_end, domain=None, range=Optional[Union[int, Position]])

slots.hasSpan__subject_label = Slot(uri=ANN.subject_label, name="hasSpan__subject_label", curie=ANN.curie('subject_label'),
                   model_uri=ANN.hasSpan__subject_label, domain=None, range=Optional[str])

slots.hasSpan__subject_source = Slot(uri=SSSOM.subject_source, name="hasSpan__subject_source", curie=SSSOM.curie('subject_source'),
                   model_uri=ANN.hasSpan__subject_source, domain=None, range=Optional[str])

slots.hasSpan__subject_text_id = Slot(uri=ANN.subject_text_id, name="hasSpan__subject_text_id", curie=ANN.curie('subject_text_id'),
                   model_uri=ANN.hasSpan__subject_text_id, domain=None, range=Optional[Union[str, TextualElementId]])

slots.textAnnotation__predicate_id = Slot(uri=SSSOM.predicate_id, name="textAnnotation__predicate_id", curie=SSSOM.curie('predicate_id'),
                   model_uri=ANN.textAnnotation__predicate_id, domain=None, range=Optional[str])

slots.textAnnotation__object_id = Slot(uri=SSSOM.object_id, name="textAnnotation__object_id", curie=SSSOM.curie('object_id'),
                   model_uri=ANN.textAnnotation__object_id, domain=None, range=Optional[str])

slots.textAnnotation__object_label = Slot(uri=SSSOM.object_label, name="textAnnotation__object_label", curie=SSSOM.curie('object_label'),
                   model_uri=ANN.textAnnotation__object_label, domain=None, range=Optional[str])

slots.textAnnotation__object_source = Slot(uri=SSSOM.object_source, name="textAnnotation__object_source", curie=SSSOM.curie('object_source'),
                   model_uri=ANN.textAnnotation__object_source, domain=None, range=Optional[str])

slots.textAnnotation__confidence = Slot(uri=SSSOM.confidence, name="textAnnotation__confidence", curie=SSSOM.curie('confidence'),
                   model_uri=ANN.textAnnotation__confidence, domain=None, range=Optional[float])

slots.textAnnotation__match_string = Slot(uri=SSSOM.match_string, name="textAnnotation__match_string", curie=SSSOM.curie('match_string'),
                   model_uri=ANN.textAnnotation__match_string, domain=None, range=Optional[str])

slots.textAnnotation__is_longest_match = Slot(uri=ANN.is_longest_match, name="textAnnotation__is_longest_match", curie=ANN.curie('is_longest_match'),
                   model_uri=ANN.textAnnotation__is_longest_match, domain=None, range=Optional[Union[bool, Bool]])

slots.textAnnotation__matches_whole_text = Slot(uri=ANN.matches_whole_text, name="textAnnotation__matches_whole_text", curie=ANN.curie('matches_whole_text'),
                   model_uri=ANN.textAnnotation__matches_whole_text, domain=None, range=Optional[Union[bool, Bool]])

slots.textAnnotation__match_type = Slot(uri=ANN.match_type, name="textAnnotation__match_type", curie=ANN.curie('match_type'),
                   model_uri=ANN.textAnnotation__match_type, domain=None, range=Optional[str])

slots.textAnnotation__info = Slot(uri=ANN.info, name="textAnnotation__info", curie=ANN.curie('info'),
                   model_uri=ANN.textAnnotation__info, domain=None, range=Optional[str])
