pip install weibull

import weibull

cycles=(146,104,150,100,150,150)

analysis = weibull.Analysis(cycles, unit='cycle')

analysis.fit(method='lr', confidence_level=0.9)

analysis.stats

analysis.probplot()

analysis.sf()