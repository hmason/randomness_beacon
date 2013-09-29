NIST Randomness Beacon
======================

This is a python module to simplify using the [NIST randomness beacon](http://www.nist.gov/itl/csd/ct/nist_beacon.cfm), a public source of truly random numbers. 

From the project description:

> The Beacon will broadcast full-entropy bit-strings in blocks of 512 bits every 60 seconds. Each such value is time-stamped and signed, and includes the hash of the previous value to chain the sequence of values together.

Using the python wrapper is easy. To generate a random number:

    b = Beacon()
    print b.last_record()['outputValue']
  
The Beacon object will cache the timestamp of the last call and use that for the basis of next() and previous() calls.
    
There's also a generator for convenience:

    for num in random_nums(3):
        print num['outputValue']

(Note, as the documentation says, *WARNING: DO NOT USE BEACON GENERATED VALUES AS SECRET CRYPTOGRAPHIC KEYS.*)
