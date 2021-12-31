# The PEP 484 type hints stub file for the QtMultimedia module.
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

from PyQt4 import QtGui
from PyQt4 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Support for old-style signals and slots.
QT_SIGNAL = str
QT_SLOT = str


class QAbstractVideoBuffer(sip.simplewrapper):

    class MapMode(int): ...
    NotMapped = ... # type: 'QAbstractVideoBuffer.MapMode'
    ReadOnly = ... # type: 'QAbstractVideoBuffer.MapMode'
    WriteOnly = ... # type: 'QAbstractVideoBuffer.MapMode'
    ReadWrite = ... # type: 'QAbstractVideoBuffer.MapMode'

    class HandleType(int): ...
    NoHandle = ... # type: 'QAbstractVideoBuffer.HandleType'
    GLTextureHandle = ... # type: 'QAbstractVideoBuffer.HandleType'
    XvShmImageHandle = ... # type: 'QAbstractVideoBuffer.HandleType'
    CoreImageHandle = ... # type: 'QAbstractVideoBuffer.HandleType'
    QPixmapHandle = ... # type: 'QAbstractVideoBuffer.HandleType'
    UserHandle = ... # type: 'QAbstractVideoBuffer.HandleType'

    def __init__(self, type: 'QAbstractVideoBuffer.HandleType') -> None: ...

    def handle(self) -> typing.Any: ...
    def unmap(self) -> None: ...
    def map(self, mode: 'QAbstractVideoBuffer.MapMode') -> typing.Tuple[sip.voidptr, int, int]: ...
    def mapMode(self) -> 'QAbstractVideoBuffer.MapMode': ...
    def handleType(self) -> 'QAbstractVideoBuffer.HandleType': ...


class QAbstractVideoSurface(QtCore.QObject):

    class Error(int): ...
    NoError = ... # type: 'QAbstractVideoSurface.Error'
    UnsupportedFormatError = ... # type: 'QAbstractVideoSurface.Error'
    IncorrectFormatError = ... # type: 'QAbstractVideoSurface.Error'
    StoppedError = ... # type: 'QAbstractVideoSurface.Error'
    ResourceError = ... # type: 'QAbstractVideoSurface.Error'

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def setError(self, error: 'QAbstractVideoSurface.Error') -> None: ...
    def supportedFormatsChanged(self) -> None: ...
    def surfaceFormatChanged(self, format: 'QVideoSurfaceFormat') -> None: ...
    def activeChanged(self, active: bool) -> None: ...
    def error(self) -> 'QAbstractVideoSurface.Error': ...
    def present(self, frame: 'QVideoFrame') -> bool: ...
    def isActive(self) -> bool: ...
    def stop(self) -> None: ...
    def start(self, format: 'QVideoSurfaceFormat') -> bool: ...
    def surfaceFormat(self) -> 'QVideoSurfaceFormat': ...
    def nearestFormat(self, format: 'QVideoSurfaceFormat') -> 'QVideoSurfaceFormat': ...
    def isFormatSupported(self, format: 'QVideoSurfaceFormat') -> bool: ...
    def supportedPixelFormats(self, type: QAbstractVideoBuffer.HandleType = ...) -> typing.List['QVideoFrame.PixelFormat']: ...


class QAudio(sip.simplewrapper):

    class Mode(int): ...
    AudioInput = ... # type: 'QAudio.Mode'
    AudioOutput = ... # type: 'QAudio.Mode'

    class State(int): ...
    ActiveState = ... # type: 'QAudio.State'
    SuspendedState = ... # type: 'QAudio.State'
    StoppedState = ... # type: 'QAudio.State'
    IdleState = ... # type: 'QAudio.State'

    class Error(int): ...
    NoError = ... # type: 'QAudio.Error'
    OpenError = ... # type: 'QAudio.Error'
    IOError = ... # type: 'QAudio.Error'
    UnderrunError = ... # type: 'QAudio.Error'
    FatalError = ... # type: 'QAudio.Error'


class QAudioDeviceInfo(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QAudioDeviceInfo') -> None: ...

    def supportedChannelCounts(self) -> typing.List[int]: ...
    def supportedSampleRates(self) -> typing.List[int]: ...
    @staticmethod
    def availableDevices(mode: QAudio.Mode) -> typing.List['QAudioDeviceInfo']: ...
    @staticmethod
    def defaultOutputDevice() -> 'QAudioDeviceInfo': ...
    @staticmethod
    def defaultInputDevice() -> 'QAudioDeviceInfo': ...
    def supportedSampleTypes(self) -> typing.List['QAudioFormat.SampleType']: ...
    def supportedByteOrders(self) -> typing.List['QAudioFormat.Endian']: ...
    def supportedSampleSizes(self) -> typing.List[int]: ...
    def supportedChannels(self) -> typing.List[int]: ...
    def supportedFrequencies(self) -> typing.List[int]: ...
    def supportedCodecs(self) -> typing.List[str]: ...
    def nearestFormat(self, format: 'QAudioFormat') -> 'QAudioFormat': ...
    def preferredFormat(self) -> 'QAudioFormat': ...
    def isFormatSupported(self, format: 'QAudioFormat') -> bool: ...
    def deviceName(self) -> str: ...
    def isNull(self) -> bool: ...


class QAudioFormat(sip.simplewrapper):

    class Endian(int): ...
    BigEndian = ... # type: 'QAudioFormat.Endian'
    LittleEndian = ... # type: 'QAudioFormat.Endian'

    class SampleType(int): ...
    Unknown = ... # type: 'QAudioFormat.SampleType'
    SignedInt = ... # type: 'QAudioFormat.SampleType'
    UnSignedInt = ... # type: 'QAudioFormat.SampleType'
    Float = ... # type: 'QAudioFormat.SampleType'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QAudioFormat') -> None: ...

    def channelCount(self) -> int: ...
    def setChannelCount(self, channelCount: int) -> None: ...
    def sampleRate(self) -> int: ...
    def setSampleRate(self, sampleRate: int) -> None: ...
    def sampleType(self) -> 'QAudioFormat.SampleType': ...
    def setSampleType(self, sampleType: 'QAudioFormat.SampleType') -> None: ...
    def byteOrder(self) -> 'QAudioFormat.Endian': ...
    def setByteOrder(self, byteOrder: 'QAudioFormat.Endian') -> None: ...
    def codec(self) -> str: ...
    def setCodec(self, codec: str) -> None: ...
    def sampleSize(self) -> int: ...
    def setSampleSize(self, sampleSize: int) -> None: ...
    def channels(self) -> int: ...
    def setChannels(self, channels: int) -> None: ...
    def frequency(self) -> int: ...
    def setFrequency(self, frequency: int) -> None: ...
    def isValid(self) -> bool: ...


class QAudioInput(QtCore.QObject):

    @typing.overload
    def __init__(self, format: QAudioFormat = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, audioDevice: QAudioDeviceInfo, format: QAudioFormat = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def notify(self) -> None: ...
    def stateChanged(self, a0: QAudio.State) -> None: ...
    def state(self) -> QAudio.State: ...
    def error(self) -> QAudio.Error: ...
    def elapsedUSecs(self) -> int: ...
    def processedUSecs(self) -> int: ...
    def notifyInterval(self) -> int: ...
    def setNotifyInterval(self, milliSeconds: int) -> None: ...
    def periodSize(self) -> int: ...
    def bytesReady(self) -> int: ...
    def bufferSize(self) -> int: ...
    def setBufferSize(self, bytes: int) -> None: ...
    def resume(self) -> None: ...
    def suspend(self) -> None: ...
    def reset(self) -> None: ...
    def stop(self) -> None: ...
    @typing.overload
    def start(self, device: QtCore.QIODevice) -> None: ...
    @typing.overload
    def start(self) -> QtCore.QIODevice: ...
    def format(self) -> QAudioFormat: ...


class QAudioOutput(QtCore.QObject):

    @typing.overload
    def __init__(self, format: QAudioFormat = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, audioDevice: QAudioDeviceInfo, format: QAudioFormat = ..., parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def notify(self) -> None: ...
    def stateChanged(self, a0: QAudio.State) -> None: ...
    def state(self) -> QAudio.State: ...
    def error(self) -> QAudio.Error: ...
    def elapsedUSecs(self) -> int: ...
    def processedUSecs(self) -> int: ...
    def notifyInterval(self) -> int: ...
    def setNotifyInterval(self, milliSeconds: int) -> None: ...
    def periodSize(self) -> int: ...
    def bytesFree(self) -> int: ...
    def bufferSize(self) -> int: ...
    def setBufferSize(self, bytes: int) -> None: ...
    def resume(self) -> None: ...
    def suspend(self) -> None: ...
    def reset(self) -> None: ...
    def stop(self) -> None: ...
    @typing.overload
    def start(self, device: QtCore.QIODevice) -> None: ...
    @typing.overload
    def start(self) -> QtCore.QIODevice: ...
    def format(self) -> QAudioFormat: ...


class QVideoFrame(sip.simplewrapper):

    class PixelFormat(int): ...
    Format_Invalid = ... # type: 'QVideoFrame.PixelFormat'
    Format_ARGB32 = ... # type: 'QVideoFrame.PixelFormat'
    Format_ARGB32_Premultiplied = ... # type: 'QVideoFrame.PixelFormat'
    Format_RGB32 = ... # type: 'QVideoFrame.PixelFormat'
    Format_RGB24 = ... # type: 'QVideoFrame.PixelFormat'
    Format_RGB565 = ... # type: 'QVideoFrame.PixelFormat'
    Format_RGB555 = ... # type: 'QVideoFrame.PixelFormat'
    Format_ARGB8565_Premultiplied = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGRA32 = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGRA32_Premultiplied = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGR32 = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGR24 = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGR565 = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGR555 = ... # type: 'QVideoFrame.PixelFormat'
    Format_BGRA5658_Premultiplied = ... # type: 'QVideoFrame.PixelFormat'
    Format_AYUV444 = ... # type: 'QVideoFrame.PixelFormat'
    Format_AYUV444_Premultiplied = ... # type: 'QVideoFrame.PixelFormat'
    Format_YUV444 = ... # type: 'QVideoFrame.PixelFormat'
    Format_YUV420P = ... # type: 'QVideoFrame.PixelFormat'
    Format_YV12 = ... # type: 'QVideoFrame.PixelFormat'
    Format_UYVY = ... # type: 'QVideoFrame.PixelFormat'
    Format_YUYV = ... # type: 'QVideoFrame.PixelFormat'
    Format_NV12 = ... # type: 'QVideoFrame.PixelFormat'
    Format_NV21 = ... # type: 'QVideoFrame.PixelFormat'
    Format_IMC1 = ... # type: 'QVideoFrame.PixelFormat'
    Format_IMC2 = ... # type: 'QVideoFrame.PixelFormat'
    Format_IMC3 = ... # type: 'QVideoFrame.PixelFormat'
    Format_IMC4 = ... # type: 'QVideoFrame.PixelFormat'
    Format_Y8 = ... # type: 'QVideoFrame.PixelFormat'
    Format_Y16 = ... # type: 'QVideoFrame.PixelFormat'
    Format_User = ... # type: 'QVideoFrame.PixelFormat'

    class FieldType(int): ...
    ProgressiveFrame = ... # type: 'QVideoFrame.FieldType'
    TopField = ... # type: 'QVideoFrame.FieldType'
    BottomField = ... # type: 'QVideoFrame.FieldType'
    InterlacedFrame = ... # type: 'QVideoFrame.FieldType'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, buffer: QAbstractVideoBuffer, size: QtCore.QSize, format: 'QVideoFrame.PixelFormat') -> None: ...
    @typing.overload
    def __init__(self, bytes: int, size: QtCore.QSize, bytesPerLine: int, format: 'QVideoFrame.PixelFormat') -> None: ...
    @typing.overload
    def __init__(self, image: QtGui.QImage) -> None: ...
    @typing.overload
    def __init__(self, other: 'QVideoFrame') -> None: ...

    @staticmethod
    def imageFormatFromPixelFormat(format: 'QVideoFrame.PixelFormat') -> QtGui.QImage.Format: ...
    @staticmethod
    def pixelFormatFromImageFormat(format: QtGui.QImage.Format) -> 'QVideoFrame.PixelFormat': ...
    def setEndTime(self, time: int) -> None: ...
    def endTime(self) -> int: ...
    def setStartTime(self, time: int) -> None: ...
    def startTime(self) -> int: ...
    def handle(self) -> typing.Any: ...
    def mappedBytes(self) -> int: ...
    def bits(self) -> sip.voidptr: ...
    def bytesPerLine(self) -> int: ...
    def unmap(self) -> None: ...
    def map(self, mode: QAbstractVideoBuffer.MapMode) -> bool: ...
    def mapMode(self) -> QAbstractVideoBuffer.MapMode: ...
    def isWritable(self) -> bool: ...
    def isReadable(self) -> bool: ...
    def isMapped(self) -> bool: ...
    def setFieldType(self, a0: 'QVideoFrame.FieldType') -> None: ...
    def fieldType(self) -> 'QVideoFrame.FieldType': ...
    def height(self) -> int: ...
    def width(self) -> int: ...
    def size(self) -> QtCore.QSize: ...
    def handleType(self) -> QAbstractVideoBuffer.HandleType: ...
    def pixelFormat(self) -> 'QVideoFrame.PixelFormat': ...
    def isValid(self) -> bool: ...


class QVideoSurfaceFormat(sip.simplewrapper):

    class YCbCrColorSpace(int): ...
    YCbCr_Undefined = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'
    YCbCr_BT601 = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'
    YCbCr_BT709 = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'
    YCbCr_xvYCC601 = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'
    YCbCr_xvYCC709 = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'
    YCbCr_JPEG = ... # type: 'QVideoSurfaceFormat.YCbCrColorSpace'

    class Direction(int): ...
    TopToBottom = ... # type: 'QVideoSurfaceFormat.Direction'
    BottomToTop = ... # type: 'QVideoSurfaceFormat.Direction'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, size: QtCore.QSize, format: QVideoFrame.PixelFormat, type: QAbstractVideoBuffer.HandleType = ...) -> None: ...
    @typing.overload
    def __init__(self, format: 'QVideoSurfaceFormat') -> None: ...

    def setProperty(self, name: str, value: typing.Any) -> None: ...
    def property(self, name: str) -> typing.Any: ...
    def propertyNames(self) -> typing.List[QtCore.QByteArray]: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def setYCbCrColorSpace(self, colorSpace: 'QVideoSurfaceFormat.YCbCrColorSpace') -> None: ...
    def yCbCrColorSpace(self) -> 'QVideoSurfaceFormat.YCbCrColorSpace': ...
    @typing.overload
    def setPixelAspectRatio(self, ratio: QtCore.QSize) -> None: ...
    @typing.overload
    def setPixelAspectRatio(self, width: int, height: int) -> None: ...
    def pixelAspectRatio(self) -> QtCore.QSize: ...
    def setFrameRate(self, rate: float) -> None: ...
    def frameRate(self) -> float: ...
    def setScanLineDirection(self, direction: 'QVideoSurfaceFormat.Direction') -> None: ...
    def scanLineDirection(self) -> 'QVideoSurfaceFormat.Direction': ...
    def setViewport(self, viewport: QtCore.QRect) -> None: ...
    def viewport(self) -> QtCore.QRect: ...
    def frameHeight(self) -> int: ...
    def frameWidth(self) -> int: ...
    @typing.overload
    def setFrameSize(self, size: QtCore.QSize) -> None: ...
    @typing.overload
    def setFrameSize(self, width: int, height: int) -> None: ...
    def frameSize(self) -> QtCore.QSize: ...
    def handleType(self) -> QAbstractVideoBuffer.HandleType: ...
    def pixelFormat(self) -> QVideoFrame.PixelFormat: ...
    def isValid(self) -> bool: ...
