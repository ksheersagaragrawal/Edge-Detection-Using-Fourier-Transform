# An Implementation of DFT Algorithm in Python

def DFT(f):
  N = len(f)
  
  # we are creating a empty array of 0s of size N
  F = np.zeros(N).astype(np.complex64)
  
  # creating indices for x, allowing to compute the multiplication using
  numpy (f*exp)
  x = np.arange(N)

  # for each frequency 'u', perform vectorial multiplication and sum
  # doing 4N - 2 operations N times → O(n complexity 2)

  for freq in np.arange(N):
    F[freq] = np.sum(f*np.exp((-1j*2*np.pi*freq*x)/N))
 
  return dft_F
