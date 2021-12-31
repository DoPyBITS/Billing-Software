# The PEP 484 type hints stub file for the QtXmlPatterns module.
#
# Generated by SIP 4.19.21
#
# Copyright (c) 2018 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt4.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt4 import QtNetwork
from PyQt4 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Support for old-style signals and slots.
QT_SIGNAL = str
QT_SLOT = str


class QAbstractMessageHandler(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def handleMessage(self, type: QtCore.QtMsgType, description: str, identifier: QtCore.QUrl, sourceLocation: 'QSourceLocation') -> None: ...
    def message(self, type: QtCore.QtMsgType, description: str, identifier: QtCore.QUrl = ..., sourceLocation: 'QSourceLocation' = ...) -> None: ...


class QAbstractUriResolver(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def resolve(self, relative: QtCore.QUrl, baseURI: QtCore.QUrl) -> QtCore.QUrl: ...


class QXmlNodeModelIndex(sip.simplewrapper):

    class DocumentOrder(int): ...
    Precedes = ... # type: 'QXmlNodeModelIndex.DocumentOrder'
    Is = ... # type: 'QXmlNodeModelIndex.DocumentOrder'
    Follows = ... # type: 'QXmlNodeModelIndex.DocumentOrder'

    class NodeKind(int): ...
    Attribute = ... # type: 'QXmlNodeModelIndex.NodeKind'
    Comment = ... # type: 'QXmlNodeModelIndex.NodeKind'
    Document = ... # type: 'QXmlNodeModelIndex.NodeKind'
    Element = ... # type: 'QXmlNodeModelIndex.NodeKind'
    Namespace = ... # type: 'QXmlNodeModelIndex.NodeKind'
    ProcessingInstruction = ... # type: 'QXmlNodeModelIndex.NodeKind'
    Text = ... # type: 'QXmlNodeModelIndex.NodeKind'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QXmlNodeModelIndex') -> None: ...

    def __hash__(self) -> int: ...
    def isNull(self) -> bool: ...
    def additionalData(self) -> int: ...
    def model(self) -> 'QAbstractXmlNodeModel': ...
    def internalPointer(self) -> typing.Any: ...
    def data(self) -> int: ...


class QAbstractXmlNodeModel(sip.simplewrapper):

    class SimpleAxis(int): ...
    Parent = ... # type: 'QAbstractXmlNodeModel.SimpleAxis'
    FirstChild = ... # type: 'QAbstractXmlNodeModel.SimpleAxis'
    PreviousSibling = ... # type: 'QAbstractXmlNodeModel.SimpleAxis'
    NextSibling = ... # type: 'QAbstractXmlNodeModel.SimpleAxis'

    def __init__(self) -> None: ...

    @typing.overload
    def createIndex(self, data: int) -> QXmlNodeModelIndex: ...
    @typing.overload
    def createIndex(self, data: int, additionalData: int) -> QXmlNodeModelIndex: ...
    @typing.overload
    def createIndex(self, pointer: typing.Any, additionalData: int = ...) -> QXmlNodeModelIndex: ...
    def attributes(self, element: QXmlNodeModelIndex) -> typing.List[QXmlNodeModelIndex]: ...
    def nextFromSimpleAxis(self, axis: 'QAbstractXmlNodeModel.SimpleAxis', origin: QXmlNodeModelIndex) -> QXmlNodeModelIndex: ...
    def sourceLocation(self, index: QXmlNodeModelIndex) -> 'QSourceLocation': ...
    def nodesByIdref(self, NCName: 'QXmlName') -> typing.List[QXmlNodeModelIndex]: ...
    def elementById(self, NCName: 'QXmlName') -> QXmlNodeModelIndex: ...
    def namespaceBindings(self, n: QXmlNodeModelIndex) -> typing.List['QXmlName']: ...
    def typedValue(self, n: QXmlNodeModelIndex) -> typing.Any: ...
    def stringValue(self, n: QXmlNodeModelIndex) -> str: ...
    def name(self, ni: QXmlNodeModelIndex) -> 'QXmlName': ...
    def root(self, n: QXmlNodeModelIndex) -> QXmlNodeModelIndex: ...
    def compareOrder(self, ni1: QXmlNodeModelIndex, ni2: QXmlNodeModelIndex) -> QXmlNodeModelIndex.DocumentOrder: ...
    def kind(self, ni: QXmlNodeModelIndex) -> QXmlNodeModelIndex.NodeKind: ...
    def documentUri(self, ni: QXmlNodeModelIndex) -> QtCore.QUrl: ...
    def baseUri(self, ni: QXmlNodeModelIndex) -> QtCore.QUrl: ...


class QXmlItem(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QXmlItem') -> None: ...
    @typing.overload
    def __init__(self, node: QXmlNodeModelIndex) -> None: ...
    @typing.overload
    def __init__(self, atomicValue: typing.Any) -> None: ...

    def toNodeModelIndex(self) -> QXmlNodeModelIndex: ...
    def toAtomicValue(self) -> typing.Any: ...
    def isAtomicValue(self) -> bool: ...
    def isNode(self) -> bool: ...
    def isNull(self) -> bool: ...


class QAbstractXmlReceiver(sip.simplewrapper):

    def __init__(self) -> None: ...

    def endOfSequence(self) -> None: ...
    def startOfSequence(self) -> None: ...
    def namespaceBinding(self, name: 'QXmlName') -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def processingInstruction(self, target: 'QXmlName', value: str) -> None: ...
    def endDocument(self) -> None: ...
    def startDocument(self) -> None: ...
    def characters(self, value: str) -> None: ...
    def comment(self, value: str) -> None: ...
    def attribute(self, name: 'QXmlName', value: str) -> None: ...
    def endElement(self) -> None: ...
    def startElement(self, name: 'QXmlName') -> None: ...


class QSimpleXmlNodeModel(QAbstractXmlNodeModel):

    def __init__(self, namePool: 'QXmlNamePool') -> None: ...

    def nodesByIdref(self, idref: 'QXmlName') -> typing.List[QXmlNodeModelIndex]: ...
    def elementById(self, id: 'QXmlName') -> QXmlNodeModelIndex: ...
    def stringValue(self, node: QXmlNodeModelIndex) -> str: ...
    def namespaceBindings(self, a0: QXmlNodeModelIndex) -> typing.List['QXmlName']: ...
    def namePool(self) -> 'QXmlNamePool': ...
    def baseUri(self, node: QXmlNodeModelIndex) -> QtCore.QUrl: ...


class QSourceLocation(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QSourceLocation') -> None: ...
    @typing.overload
    def __init__(self, u: QtCore.QUrl, line: int = ..., column: int = ...) -> None: ...

    def __hash__(self) -> int: ...
    def isNull(self) -> bool: ...
    def setUri(self, newUri: QtCore.QUrl) -> None: ...
    def uri(self) -> QtCore.QUrl: ...
    def setLine(self, newLine: int) -> None: ...
    def line(self) -> int: ...
    def setColumn(self, newColumn: int) -> None: ...
    def column(self) -> int: ...


class QXmlSerializer(QAbstractXmlReceiver):

    def __init__(self, query: 'QXmlQuery', outputDevice: QtCore.QIODevice) -> None: ...

    def codec(self) -> QtCore.QTextCodec: ...
    def setCodec(self, codec: QtCore.QTextCodec) -> None: ...
    def outputDevice(self) -> QtCore.QIODevice: ...
    def endOfSequence(self) -> None: ...
    def startOfSequence(self) -> None: ...
    def endDocument(self) -> None: ...
    def startDocument(self) -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def processingInstruction(self, name: 'QXmlName', value: str) -> None: ...
    def attribute(self, name: 'QXmlName', value: str) -> None: ...
    def endElement(self) -> None: ...
    def startElement(self, name: 'QXmlName') -> None: ...
    def comment(self, value: str) -> None: ...
    def characters(self, value: str) -> None: ...
    def namespaceBinding(self, nb: 'QXmlName') -> None: ...


class QXmlFormatter(QXmlSerializer):

    def __init__(self, query: 'QXmlQuery', outputDevice: QtCore.QIODevice) -> None: ...

    def setIndentationDepth(self, depth: int) -> None: ...
    def indentationDepth(self) -> int: ...
    def endOfSequence(self) -> None: ...
    def startOfSequence(self) -> None: ...
    def endDocument(self) -> None: ...
    def startDocument(self) -> None: ...
    def atomicValue(self, value: typing.Any) -> None: ...
    def processingInstruction(self, name: 'QXmlName', value: str) -> None: ...
    def attribute(self, name: 'QXmlName', value: str) -> None: ...
    def endElement(self) -> None: ...
    def startElement(self, name: 'QXmlName') -> None: ...
    def comment(self, value: str) -> None: ...
    def characters(self, value: str) -> None: ...


class QXmlName(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, namePool: 'QXmlNamePool', localName: str, namespaceUri: str = ..., prefix: str = ...) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QXmlName') -> None: ...

    def __hash__(self) -> int: ...
    @staticmethod
    def fromClarkName(clarkName: str, namePool: 'QXmlNamePool') -> 'QXmlName': ...
    @staticmethod
    def isNCName(candidate: str) -> bool: ...
    def isNull(self) -> bool: ...
    def toClarkName(self, query: 'QXmlNamePool') -> str: ...
    def localName(self, query: 'QXmlNamePool') -> str: ...
    def prefix(self, query: 'QXmlNamePool') -> str: ...
    def namespaceUri(self, query: 'QXmlNamePool') -> str: ...


class QXmlNamePool(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QXmlNamePool') -> None: ...


class QXmlQuery(sip.simplewrapper):

    class QueryLanguage(int): ...
    XQuery10 = ... # type: 'QXmlQuery.QueryLanguage'
    XSLT20 = ... # type: 'QXmlQuery.QueryLanguage'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QXmlQuery') -> None: ...
    @typing.overload
    def __init__(self, np: QXmlNamePool) -> None: ...
    @typing.overload
    def __init__(self, queryLanguage: 'QXmlQuery.QueryLanguage', pool: QXmlNamePool = ...) -> None: ...

    def queryLanguage(self) -> 'QXmlQuery.QueryLanguage': ...
    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def setNetworkAccessManager(self, newManager: QtNetwork.QNetworkAccessManager) -> None: ...
    def initialTemplateName(self) -> QXmlName: ...
    @typing.overload
    def setInitialTemplateName(self, name: QXmlName) -> None: ...
    @typing.overload
    def setInitialTemplateName(self, name: str) -> None: ...
    @typing.overload
    def setFocus(self, item: QXmlItem) -> None: ...
    @typing.overload
    def setFocus(self, documentURI: QtCore.QUrl) -> bool: ...
    @typing.overload
    def setFocus(self, document: QtCore.QIODevice) -> bool: ...
    @typing.overload
    def setFocus(self, focus: str) -> bool: ...
    def uriResolver(self) -> QAbstractUriResolver: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def evaluateToString(self) -> str: ...
    def evaluateToStringList(self) -> typing.List[str]: ...
    @typing.overload
    def evaluateTo(self, result: 'QXmlResultItems') -> None: ...
    @typing.overload
    def evaluateTo(self, callback: QAbstractXmlReceiver) -> bool: ...
    @typing.overload
    def evaluateTo(self, target: QtCore.QIODevice) -> bool: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def bindVariable(self, name: QXmlName, value: QXmlItem) -> None: ...
    @typing.overload
    def bindVariable(self, name: QXmlName, a1: QtCore.QIODevice) -> None: ...
    @typing.overload
    def bindVariable(self, name: QXmlName, query: 'QXmlQuery') -> None: ...
    @typing.overload
    def bindVariable(self, localName: str, value: QXmlItem) -> None: ...
    @typing.overload
    def bindVariable(self, localName: str, a1: QtCore.QIODevice) -> None: ...
    @typing.overload
    def bindVariable(self, localName: str, query: 'QXmlQuery') -> None: ...
    def namePool(self) -> QXmlNamePool: ...
    @typing.overload
    def setQuery(self, sourceCode: str, documentUri: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def setQuery(self, sourceCode: QtCore.QIODevice, documentUri: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def setQuery(self, queryURI: QtCore.QUrl, baseUri: QtCore.QUrl = ...) -> None: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def setMessageHandler(self, messageHandler: QAbstractMessageHandler) -> None: ...


class QXmlResultItems(sip.simplewrapper):

    def __init__(self) -> None: ...

    def current(self) -> QXmlItem: ...
    def next(self) -> QXmlItem: ...
    def hasError(self) -> bool: ...


class QXmlSchema(sip.simplewrapper):

    def __init__(self) -> None: ...

    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def setNetworkAccessManager(self, networkmanager: QtNetwork.QNetworkAccessManager) -> None: ...
    def uriResolver(self) -> QAbstractUriResolver: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def setMessageHandler(self, handler: QAbstractMessageHandler) -> None: ...
    def documentUri(self) -> QtCore.QUrl: ...
    def namePool(self) -> QXmlNamePool: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def load(self, source: QtCore.QUrl) -> bool: ...
    @typing.overload
    def load(self, source: QtCore.QIODevice, documentUri: QtCore.QUrl = ...) -> bool: ...
    @typing.overload
    def load(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], documentUri: QtCore.QUrl = ...) -> bool: ...


class QXmlSchemaValidator(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, schema: QXmlSchema) -> None: ...

    def networkAccessManager(self) -> QtNetwork.QNetworkAccessManager: ...
    def setNetworkAccessManager(self, networkmanager: QtNetwork.QNetworkAccessManager) -> None: ...
    def uriResolver(self) -> QAbstractUriResolver: ...
    def setUriResolver(self, resolver: QAbstractUriResolver) -> None: ...
    def messageHandler(self) -> QAbstractMessageHandler: ...
    def setMessageHandler(self, handler: QAbstractMessageHandler) -> None: ...
    def schema(self) -> QXmlSchema: ...
    def namePool(self) -> QXmlNamePool: ...
    @typing.overload
    def validate(self, source: QtCore.QUrl) -> bool: ...
    @typing.overload
    def validate(self, source: QtCore.QIODevice, documentUri: QtCore.QUrl = ...) -> bool: ...
    @typing.overload
    def validate(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], documentUri: QtCore.QUrl = ...) -> bool: ...
    def setSchema(self, schema: QXmlSchema) -> None: ...
