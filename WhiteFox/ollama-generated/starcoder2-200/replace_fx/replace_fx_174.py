
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1, dtype=int)  # generate a tensor with the same size as input filled with random numbers (dtype == int)
        v3 = x1 + v2 
        return v3


# Initializing the model and generating input tensors to the model
m  = Model()
i1_cpu = torch.randn(2, 4).to('cpu')
i2_cpu = torch.randn(2, 4).to('cpu')
i1_gpu = i1_cpu.to('cuda:0') # Use cuda:0 to generate input tensors for GPU devices; otherwise use cuda:x instead. 
i2_gpu = i2_cpu.to('cuda:0') 

# Evaluating the model on the inputs of the CPU version (this is the expected execution behavior)
print(m(i1_cpu))
print(m(i2_cpu))


# Evaluating the model on the GPU 
print(m(i1_gpu)) # The GPU version must return same results as CPU.
print(m(i2_gpu)) 

