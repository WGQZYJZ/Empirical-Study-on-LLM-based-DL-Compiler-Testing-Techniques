
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()

    def forward(self, input0, input1):
        v1 = torch.cat([input0, input1], dim=1) 
        v2  = v1[:, 0:9223372036854775807] # Slice along dimension 1 of the concatenated tensor.
        v3 = v2[:, 0:size] # Further slice along dimension 1 of the sliced concatenated tensor.
        v4 = torch.cat([v1, v3], dim=1) 
        return v4


m = Model(input_shape[1])

# Inputs to the model
input1 = torch.randn(batch_size, 8 * input_shape[0], 65, 65) # First input tensor of size (batchSize x 256 x 32x32). batchSize = 4 and num_in_channels=8 in the above example. 
input2 = torch.randn(batch_size, 10 * input_shape[0], 9223372036854775807) # Second input tensor of size (batchSize x 8192 x 3x3). batchSize = 4 and num_out_channels=8 in the above example.
