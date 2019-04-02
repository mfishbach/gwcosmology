"""some basic helper functions
"""
__author__ = "maya.fishbach@ligo.org, reed.essick@ligo.org"

#-------------------------------------------------

def distance_name(): 
    "name of the distance column in the PE file"
    return 'distance'

def galaxy_name(graceid,galaxyname):
    "generate a standard filename for galaxy information"
    return "galaxy-%s-%s.json"%(graceid,galaxyname)

def h0_name(graceid,chosen_skymap,galaxyname,PE_samples=False):
    "generate a standard filename for H0 posterior"
    skyname = chosen_skymap.split('.')[0]
    if PE_samples is False:
        return "/home/maya.fishbach/public_html/cgi-bin/H0-public-%s-%s-%s.json"%(graceid,skyname,galaxyname)
    if PE_samples is True:
        return "H0-proprietary-%s-%s-%s.json"%(graceid,skyname,galaxyname)

def H0_plot_name(graceid,chosen_skymap,galaxyname):
     "generate a standard filename for H0 plot"
     skyname = chosen_skymap.split('.')[0]
     return "H0-%s-%s-%s.png"%(graceid,skyname,galaxyname)

def H0files_dict_name(private):
     "generate a standard filename for json dictionary containing all available H0 likelihoods"
     if private is True:
         return "/home/maya.fishbach/public_html/manifest-private.json"
     else:
         return "/home/maya.fishbach/public_html/manifest-public.json"

