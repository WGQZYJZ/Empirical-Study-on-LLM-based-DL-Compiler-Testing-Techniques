
model = ...
input_tensor  = torch.rand((1, 32))
input_tensors = input_tensor

# Initializing the model
model = torchdynamo.enable(__name__)(Model()) # Run this with torchdynamo.enable("nnapi") to see what is the original input shape

