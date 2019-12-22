from optparse import OptionParser

parser = OptionParser()

parser.add_option("-s", "--speed", type="int", dest="speed")
(options, args) = parser.parse_args()
print(options)
print(args)

print(options.speed)
