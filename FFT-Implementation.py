# A Divide and Conquer implementation of the Fast Fourier Transform Algorithm in Python

def FFT(f):
  N = len(f)
  if (N == 0 or N == 1):
    return f
  # taking the elements at odd and even position separately
  evenarr=FFT(f[0::2])
  oddarr=FFT(f[1::2])
  
  # stores the final array containing the array after FFT is used
  ans = np.zeros(N).astype(np.complex64)
  
  # only required to compute for half the frequencies
  # since u+N/2 can be obtained from the symmetry property
  for u in range(N//2):
    ans[u]=evenarr[u]+exp(-2j*pi*u/N)*oddarr[u] # conquer
    ans[u+N//2]=evenarr[u]-exp(-2j*pi*u/N)*oddarr[u] # conquer
  
  return ans
