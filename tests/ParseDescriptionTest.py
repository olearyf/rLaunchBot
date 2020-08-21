"""
    Frances O'Leary, 8/21/2020

    I have a problem to solve. The NASA API returns
    a long string as the description to go along with an
    APOD photo. For a thread, I can only tweet a maximum of
    262 characters per tweet. Right now I just chop up my strings
    without caring if I cut a word in two. To fix this, I'm
    trying out a new parseExplanation function

    The first thing I'm going to try to do is just keep
    from chopping up words. The original is in currentParseExplanation
    and the new solution is in newParseExplanation.
"""
testExplanations = [
    "Shrouded in a thick atmosphere, Saturn's largest moon Titan really is hard to see. Small particles suspended in the upper atmosphere cause an almost impenetrable haze, strongly scattering light at visible wavelengths and hiding Titan's surface features from prying eyes. But Titan's surface is better imaged at infrared wavelengths where scattering is weaker and atmospheric absorption is reduced. Arrayed around this visible light image (center) of Titan are some of the clearest global infrared views of the tantalizing moon so far. In false color, the six panels present a consistent processing of 13 years of infrared image data from the Visual and Infrared Mapping Spectrometer (VIMS) on board the Cassini spacecraft. They offer a stunning comparison with Cassini's visible light view.   Experts Debate: How will humanity first discover extraterrestrial life?",
    "Do other stars have planets like our Sun? Previous evidence shows that they do, coming mostly from slight shifts in the star's light created by the orbiting planets.  Recently, however, and for the first time, a pair of planets has been directly imaged around a Sun-like star.  These exoplanets orbit the star designated TYC 8998-760-1 and are identified by arrows in the featured infrared image.  At 17 million years old, the parent star is much younger than the 5-billion-year age of our Sun.  Also, the exoplanets are both more massive and orbit further out than their Solar System analogues: Jupiter and Saturn. The exoplanets were found by the ESO's Very Large Telescope in Chile by their infrared glow – after the light from their parent star was artificially blocked.  As telescope and technology improve over the next decade, it is hoped that planets more closely resembling our Earth will be directly imaged.    Experts Debate: How will humanity first discover extraterrestrial life?",
    "Why would meteor trails appear curved? The arcing effect arises only because the image artificially compresses (nearly) the whole sky into a rectangle. The meteors are from the Perseid Meteor Shower that peaked last week. The featured multi-frame image combines not only different directions from the 360 projection, but different times when bright Perseid meteors momentarily streaked across the sky. All Perseid meteors can be traced back to the constellation Perseus toward the lower left, even the seemingly curved (but really straight) meteor trails.  Although Perseids always point back to their Perseus radiant, they can appear almost anywhere on the sky. The image was taken from Inner Mongolia, China, where grasslands meet sand dunes. Many treasures also visible in the busy night sky including the central arch of our Milky Way Galaxy, the planets Saturn and Jupiter toward the right, colorful airglow on the central left, and some relatively nearby Earthly clouds.  The Perseid Meteor Shower peaks every August.    Perseid Meteor Shower: Notable images submitted to APOD",
    "In the center of this serene stellar swirl is likely a harrowing black-hole beast.  The surrounding swirl sweeps around billions of stars which are highlighted by the brightest and bluest. The breadth and beauty of the display give the swirl the designation of a grand design spiral galaxy. The central beast shows evidence that it is a supermassive black hole about 10 million times the mass of  our Sun.  This ferocious creature devours stars and gas and is surrounded by a spinning moat of hot plasma that emits blasts of X-rays. The central violent activity gives it the designation of a Seyfert galaxy. Together, this beauty and beast are cataloged as NGC 6814 and have been appearing together toward the constellation of the Eagle (Aquila) for roughly the past billion years.   Pereid Meteor Shower: Notable images submitted to APOD",
    "Does the Moon ever block out Mars? Yes, the Moon occasionally moves in front of all of the Solar System's planets.  Just this past Sunday, as visible from some locations in South America, a waning gibbous Moon eclipsed Mars.  The featured image from Córdoba, Argentina captured this occultation well, showing a familiar cratered Moon in the foreground with the bright planet Mars unusually adjacent.  Within a few seconds, Mars then disappeared behind the Moon, only to reappear a few minutes later across the Moon.  Today the Moon moves close to, but not in front of, Venus.  Because alignments will not have changed by much, the next two times the Moon passes through this part of the sky – in early September and early October – it will also occult Mars, as seen from parts of South America.    Pereid Meteor Shower: Notable images submitted to APOD"
]
def currentParseExplanation(explanation):
    n = 262
    chunks = [explanation[i:i + n] for i in range(0, len(explanation), n)]
    return chunks

def newParseExplanation(explanation):
    n = 262
    explanationLength = len(explanation)
    if explanationLength < 262:
        return explanation
    chunks = []
    while 1:
        testChunk = explanation[:262]
        if len(testChunk == 262):
            lastWordIndex = testChunk.rfind(' ')
            chunks.append(explanation[:lastWordIndex])
            explanation = [lastWordIndex:]
        else:
            chunks.append(testChunk)
            break

    return chunks

def printChunks(chunks):
    print "Start of chunks:"
    for chunk in chunks:
        print "_____________________"
        print chunk
    print "_____________________"
    print "End of chunks."