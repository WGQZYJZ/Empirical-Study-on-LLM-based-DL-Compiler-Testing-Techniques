# Input tensors should be different in different runs if the model uses PyTorch APIs that can produce different output values even on the same inputs.
if __output__2_1 is not __output__1_1:
    print('Test failed.')


print('Test passed!')
# Output tensors should be different in different runs if the model uses PyTorch APIs that can produce different output values even on the same inputs.
if __output__2_1 is not __output__2_2:
    print('Test failed.')


print('Test passed!')
