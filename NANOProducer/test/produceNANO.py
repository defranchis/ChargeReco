# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename produceNano2016UL_cfg.py --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --fileout file:nanox2016.root --conditions 106X_mcRun2_asymptotic_v17 --step NANO --filein /store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/8673D920-D951-E648-A9BE-5F177802CD5B.root --era Run2_2016,run2_nanoAOD_106Xv1 --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
from Configuration.StandardSequences.Eras import eras


options = VarParsing ('analysis')

options.register(
    'isData',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "is data"
)

options.register(
    'addSignalLHE',
    True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "adds LHE weights of signal samples"
)

options.register(
    'year',
    '2016',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "add year file"
)
options.parseArguments() 

print "Year:", options.year
print "isData:", options.isData


if options.year not in ['2016','2016preVFP','2017','2018']:
    raise Exception('Year options needs to be one of the following: '+str(['2016','2016preVFP','2017','2018']))

if options.year=='2016' or options.year=='2016preVFP':
    process = cms.Process('NANO',eras.Run2_2016,eras.run2_nanoAOD_106Xv1)
elif options.year=='2017':
    process = cms.Process('NANO',eras.Run2_2017,eras.run2_nanoAOD_106Xv1)
elif options.year=='2018':
    process = cms.Process('NANO',eras.Run2_2018,eras.run2_nanoAOD_106Xv1)



# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

if options.isData:
    process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
    dataTier = cms.untracked.string('NANOAOD')
else:
    process.load('Configuration.StandardSequences.MagneticField_cff')
    dataTier = cms.untracked.string('NANOAODSIM')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

inputFiles = {
    '2016preVFP': {
        'mc': ['/store/mc/RunIISummer20UL16MiniAODAPV/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v1/270000/F8E1C8DC-C55C-0141-86A6-9BA6ED714733.root'],
        'data': ['?']
    },
    '2016': {
        'mc': ['/store/mc/RunIISummer20UL16MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/260000/8673D920-D951-E648-A9BE-5F177802CD5B.root'],
        'data': ['?'],
    },
    '2017': {
        'mc': ['/store/mc/RunIISummer19UL17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/260000/F27A3A53-2B4C-E846-B8E2-440CC8FCD255.root'],
        'data': ['?'],
    },
    '2018': {
        'mc': ['/store/mc/RunIISummer19UL18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/100000/0537A477-C32D-154E-9A17-A4792914E8B6.root'],
        'data': ['?']
    }
}


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
)

if options.isData:
    process.source.fileNames = inputFiles[options.year]['data']
else:
    process.source.fileNames = inputFiles[options.year]['mc']


process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    saveProvenance = cms.untracked.bool(True),
    fakeNameForCrab = cms.untracked.bool(True),
    dataset = cms.untracked.PSet(
        dataTier = dataTier,
        filterName = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring(
            ['wbwbxnanoAOD_step_mu','wbwbxnanoAOD_step_ele'] if options.isData else ['wbwbxnanoAOD_step']
        ) #only events passing this path will be saved
    ),
    fileName = cms.untracked.string('nanox.root'),
    #outputCommands = process.NANOAODSIMEventContent.outputCommands+cms.untracked.vstring(
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'keep nanoaodFlatTable_*Table_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep String_*_genModel_*', 
        'keep nanoaodMergeableCounterTable_*Table_*_*', 
        'keep nanoaodUniqueString_nanoMetadata_*_*'
    )
)


from Configuration.AlCa.GlobalTag import GlobalTag


globalTags = {
    '2016preVFP': {
        'mc': '106X_mcRun2_asymptotic_preVFP_v11',
        'data': '106X_dataRun2_v35'
    },
    '2016': {
        'mc': '106X_mcRun2_asymptotic_v17',
        'data': '106X_dataRun2_v35',
    },
    '2017': {
        'mc': '106X_mc2017_realistic_v8',
        'data': '106X_dataRun2_v35',
    },
    '2018': {
        'mc': '106X_upgrade2018_realistic_v15_L1v1',
        'data': '106X_dataRun2_v35'
    }
}

if options.isData:
    process.GlobalTag = GlobalTag(process.GlobalTag, globalTags[options.year]['data'], '')
    jetCorrectionsAK4PFchs = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'], 'None')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, globalTags[options.year]['mc'], '')
    jetCorrectionsAK4PFchs = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
    
    

from PhysicsTools.NanoAOD.common_cff import *
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
    
updateJetCollection(
    process,
    labelName = "XTag",
    jetSource = cms.InputTag('updatedJets'),
    jetCorrections = jetCorrectionsAK4PFchs,
    pfCandidates = cms.InputTag('packedPFCandidates'),
    pvSource = cms.InputTag("offlineSlimmedPrimaryVertices"),
    svSource = cms.InputTag('slimmedSecondaryVertices'),
    muSource = cms.InputTag('slimmedMuons'),
    elSource = cms.InputTag('slimmedElectrons'),
    btagInfos = [
        'pfImpactParameterTagInfos',
        'pfInclusiveSecondaryVertexFinderTagInfos',
        'pfDeepCSVTagInfos',
    ],
    btagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags'],
    explicitJTA = False,
)

process.jetChargeTagInfos = cms.EDProducer("JetChargeTagInfoProducer",
    jets = cms.InputTag("updatedJets"),
    muonSrc  = cms.InputTag("slimmedMuons"),
    electronSrc = cms.InputTag("slimmedElectrons"),
    shallow_tag_infos = cms.InputTag('pfDeepCSVTagInfosXTag'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices")
)

process.nanoTable = cms.EDProducer("NANOProducer",
    srcJets = cms.InputTag("finalJets"),
    srcTags = cms.InputTag("jetChargeTagInfos"),
)

#redo ghost clustering since linked gen particles have been discarded
process.patJetPartons = cms.EDProducer('HadronAndPartonSelector',
     src = cms.InputTag("generator"),
     particles = cms.InputTag("prunedGenParticles"),
     partonMode = cms.string("Auto"),
     fullChainPhysPartons = cms.bool(True)
)
process.jetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
     jets = cms.InputTag("updatedJets"),
     bHadrons = cms.InputTag("patJetPartons","bHadrons"),
     cHadrons = cms.InputTag("patJetPartons","cHadrons"),
     partons = cms.InputTag("patJetPartons","physicsPartons"),
     leptons = cms.InputTag("patJetPartons","leptons"),
     jetAlgorithm = cms.string("AntiKt"),
     rParam = cms.double(0.4),
     ghostRescaling = cms.double(1e-18),
     relPtTolerance = cms.double(9999999999), #supress warning since jets are corrected; thus pt match fails
     hadronFlavourHasPriority = cms.bool(False)
)

process.jetChargeLabels = cms.EDProducer(
    "JetChargeLabelProducer",
    srcJets = cms.InputTag("updatedJets"), #need to be same input as for 'jetFlavourAssociation'
    customFlavourAssociation = cms.InputTag("jetFlavourAssociation")
)
   

process.nanoGenTable = cms.EDProducer("NANOGenProducer",
    srcJets = cms.InputTag("finalJets"),
    srcLabels = cms.InputTag("jetChargeLabels")
)
    
  

process.lheWeightsTable = cms.EDProducer(
    "LHEWeightsProducer",
    lheInfo = cms.VInputTag(cms.InputTag("externalLHEProducer"), cms.InputTag("source")),
    weightGroups = cms.PSet()
)

#mass/width reweighting
process.lheWeightsTable.weightGroups.width = cms.vstring()
for i in range(1,106):
    process.lheWeightsTable.weightGroups.width.append("rwgt_%i"%(i))
    
#PDF NNPDF3.1 NNLO hessian
process.lheWeightsTable.weightGroups.nnpdfhessian = cms.vstring()
for i in range(1048,1149):
    process.lheWeightsTable.weightGroups.nnpdfhessian.append("%i"%(i))
    
#PDF NNPDF3.1 NNLO replicas
process.lheWeightsTable.weightGroups.nnpdfreplica = cms.vstring()
for i in range(1149,1250):
    process.lheWeightsTable.weightGroups.nnpdfreplica.append("%i"%(i))
    
#scale weights
for scaleSet in [
    ['murNominal_mufNominal',range(1001,1006)],
    ['murUp_mufNominal',range(1006,1011)],
    ['murDown_mufNominal',range(1011,1016)],
    ['murNominal_mufUp',range(1016,1021)],
    ['murUp_mufUp',range(1021,1026)],
    ['murDown_mufUp',range(1026,1031)],
    ['murNominal_mufDown',range(1031,1036)],
    ['murUp_mufDown',range(1036,1041)],
    ['murDown_mufDown',range(1041,1046)],
    ['emission',range(1046,1048)],
]:
    
    setattr(process.lheWeightsTable.weightGroups,scaleSet[0],cms.vstring())
    for i in scaleSet[1]:
        getattr(process.lheWeightsTable.weightGroups,scaleSet[0]).append("%i"%(i))
  
  
  
if options.isData:
    process.selectedMuonsForFilter = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("slimmedMuons"),
        cut = cms.string("pt>25 && isGlobalMuon()")
    )
    process.selectedMuonsMinFilter = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag("selectedMuonsForFilter"),
        minNumber = cms.uint32(1)
    )
        
    process.muonFilterSequence = cms.Sequence(
        process.selectedMuonsForFilter+process.selectedMuonsMinFilter
    )


    process.selectedElectronsForFilter = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("slimmedElectrons"),
        cut = cms.string("pt>25")
    )
    process.selectedElectronsMinFilter = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag("selectedElectronsForFilter"),
        minNumber = cms.uint32(1)
    )
        
    process.electronFilterSequence = cms.Sequence(
        process.selectedElectronsForFilter+process.selectedElectronsMinFilter
    )
    
    
    process.selecteJetsForFilter = cms.EDFilter("CandViewSelector",
        src = cms.InputTag("slimmedJets"),
        cut = cms.string("pt>25")
    )
    process.selectedJetsMinFilter = cms.EDFilter("CandViewCountFilter",
        src = cms.InputTag("selecteJetsForFilter"),
        minNumber = cms.uint32(2)
    )
    
    process.jetsFilterSequence = cms.Sequence(
        process.selecteJetsForFilter+process.selectedJetsMinFilter
    )

    process.wbwbxnanoAOD_step_mu = cms.Path(
        process.muonFilterSequence+
        process.jetsFilterSequence+
        process.nanoSequence+
        process.jetChargeTagInfos+
        process.nanoTable
    )
    process.wbwbxnanoAOD_step_ele = cms.Path(
        process.electronFilterSequence+
        process.jetsFilterSequence+
        process.nanoSequence+
        process.jetChargeTagInfos+
        process.nanoTable
    )

else:
    process.wbwbxnanoAOD_step = cms.Path(
        process.nanoSequenceMC+
        process.patJetPartons+
        process.jetFlavourAssociation+
        process.jetChargeTagInfos+
        process.jetChargeLabels+
        process.nanoTable+
        process.nanoGenTable
    )
    
    if options.addSignalLHE:
        process.wbwbxnanoAOD_step += process.lheWeightsTable
  

process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOoutput_step = cms.EndPath(process.NANOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.wbwbxnanoAOD_step,process.endjob_step,process.NANOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 
process = nanoAOD_customizeMC(process)


#remove unneeded modules
modulesToRemove = [
    "HTXSCategoryTable",
    "rivetProducerHTXS",
    "l1bits",
]

for moduleName in modulesToRemove:
    if hasattr(process,moduleName):
        print "removing module: ",moduleName
        if options.isData:
            process.nanoSequence.remove(getattr(process,moduleName))
        else:
            process.nanoSequenceMC.remove(getattr(process,moduleName))
    else:
        print "module for removal not found: ",moduleName


process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))

from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

