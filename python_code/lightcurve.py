from sunpy import lightcurve
from sunpy.time import TimeRange
tr = TimeRange("2011-06-07 06:00", "2011-06-07 08:00")
goes = lightcurve.GOESLightCurve.create(tr)
goes.peek()
print('The max flux is ' + str(goes.data['xrsb'].max()) + ' at ' + str(goes.data['xrsb'].idxmax()))                                   