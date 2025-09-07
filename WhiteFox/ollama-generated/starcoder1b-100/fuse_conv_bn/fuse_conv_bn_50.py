
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # A convolution layer and a batch normalization layer are fused together. 
    conv_bn = torch.nn.functional.conv2d(...)  # Input should match with the kernel size and output shape of the first convolution layer.
    bn      = torch.nn.functional.batch_norm(...) # Output should match with the input shape and the running mean/variance of the first batch normalization layer.

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(2, 3, 4, 5)
