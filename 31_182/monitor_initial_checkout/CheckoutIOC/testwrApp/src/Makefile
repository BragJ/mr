TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += testwrSupport

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord
# Install devXxxSoft.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Compile and add the code to the support library
testwrSupport_SRCS += xxxRecord.c
testwrSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
testwrSupport_SRCS += dbSubExample.c
testwrSupport_SRCS += testwrHello.c
testwrSupport_SRCS += initTrace.c

testwrSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = testwr
# testwr.dbd will be created and installed
DBD += testwr.dbd

# testwr.dbd will be made up from these files:
testwr_DBD += base.dbd
testwr_DBD += xxxSupport.dbd
testwr_DBD += dbSubExample.dbd
testwr_DBD += testwrHello.dbd
testwr_DBD += initTrace.dbd

# testwr_registerRecordDeviceDriver.cpp derives from testwr.dbd
testwr_SRCS += testwr_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
testwr_SRCS_DEFAULT += testwrMain.cpp
testwr_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#testwr_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
testwr_LIBS += testwrSupport

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into testwrSupport
    sncExample_SNCFLAGS += +r
    testwr_DBD += sncExample.dbd
    testwrSupport_SRCS += sncExample.stt
    testwrSupport_LIBS += seq pv
    testwr_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link to the EPICS Base libraries
testwr_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

