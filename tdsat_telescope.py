def load_telescope_parameters(version, **kwargs):
    """
    Utility script to load the telescope parameters
    
    version = 0: Pre-design version (to compare with Rick's stuff)
    version = 1: 210 mm design
    version = 2: 300 mm design
    version = 3: 350 mm design
    version = 4: 400 mm design

    Syntax:
    diameter, qe, psf_fwhm, efficiency = load_telescope_parameters(version)
    
    """
    
    
    import astropy.units as ur
    from numpy import pi
    
    diag = kwargs.pop('diag', True)
    
    
    if version == 0:
        qe = 0.8 # To be improved later.
        diameter = 30*ur.cm
        psf_fwhm = 10*ur.arcsec
        efficiency = 0.87 # Ultrasat spec
    if version == 1:
        qe = 0.8
        efficiency = 0.54 # Reported from Mike  
        diameter = 21 * ur.cm
        psf_fwhm = 4 * ur.arcsec
    if version == 2:
        qe = 0.8
        efficiency = 0.65 # Reported from Mike
        diameter = 30 * ur.cm
        psf_fwhm = 9*ur.arcsec
    
    if version == 3:
        qe = 0.8
        diameter = 35*ur.cm
        efficiency = 0.67 # Reported from Mike
        psf_fwhm = 18*ur.arcsec

    if version == 4:
        qe = 0.8
        diameter = 40*ur.cm
        efficiency = 0.70 # Reported from Mike
        psf_fwhm = 23*ur.arcsec

    if diag:
        print('Telescope Configuration {}'.format(version))
        print('Entrance Pupil diameter {}'.format(diameter))
        print('Optical Effifiency {}'.format(efficiency))
        print('PSF FWHM {}'.format(psf_fwhm))
        print('Effective Aperture {}'.format(diameter*(efficiency)**0.5))
        print('Effective Area {}'.format( efficiency * pi * (0.5*diameter)**2))
              
    return diameter, qe, psf_fwhm, efficiency
    
    
def load_qe(**kwargs):
    """
    Loads the detector QE and returns the values.
    
    band = 1 (default, 180-220 nm)
    band = 2 (260-320 nm)
    band = 3 (340-380 nm)
    
    Syntax:
    
    wave, qe = load_qe(band = 1)
    
    """
    import astropy.units as ur
    import numpy as np
    
    band = kwargs.pop('band', 1)
    diag = kwargs.pop('diag', False)
    
    indir = 'input_data/'
    
    if band == 1:
        infile = indir+'detector_180_220nm.csv'
    if band == 2:
        infile = indir+'detector_260_300nm.csv'
    if band == 3:
        infile = indir+'detector_340_380nm.csv'



        
        
    f = open(infile, 'r')
    header = True
    qe = {}
    set = False
    for line in f:
        if header:
            header = False
            continue
        fields = line.split(',')
        if not set:
            wave = float(fields[0])
            qe = float(fields[3])
            set = True
        else:
            wave = np.append(wave, float(fields[0]))
            qe = np.append(qe, float(fields[3]))
 
    f.close()
    
    # Give wavelength a unit
    wave = [i*ur.nm for i in wave]
    
    if diag:
        print('Detector Q.E. loader')
        print('Band {} has input file {}'.format(band, infile))
        
    
    return wave, qe



def load_reflectivity(**kwargs):
    """
    Loads the optics reflectivity and returns the values.
    
    
    Syntax:
    
    wave, reflectivity = load_reflectivity()
    
    """
    import astropy.units as ur
    import numpy as np
    
    band = kwargs.pop('band', 1)
    diag = kwargs.pop('diag', False)
    
    indir = 'input_data/'
    
    infile = indir+'al_mgf2_mirror_coatings.csv'

    f = open(infile, 'r')
    header = True
    qe = {}
    set = False
    for line in f:
        if header:
            header = False
            continue
        fields = line.split(',')
        if not set:
            wave = float(fields[0])
            reflectivity = float(fields[1])
            set = True
        else:
            wave = np.append(wave, float(fields[0]))
            reflectivity = np.append(reflectivity, float(fields[1]))
 
    f.close()
    
    # Give wavelength a unit
    wave = [i*ur.nm for i in wave]
    
    if diag:
        print('Optics reflectivity loader')
        print('Input file {}'.format(band, infile))
        
    
    return wave, reflectivity


