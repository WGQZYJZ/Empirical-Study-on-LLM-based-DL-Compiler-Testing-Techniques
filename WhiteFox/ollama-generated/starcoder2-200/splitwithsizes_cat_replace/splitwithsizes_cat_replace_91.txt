
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        splitted = torch.split(input2, [8], 0)

        concatenated = torch.cat([splitted[i] for i in range(len(splitted))], 1)
        return concatenated


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor_1 = torch.rand(2, 4096) # The size of input_tensor_1 is [batch x 3 * 512]
input_tensor_2 = torch.rand(78, 4096) # The size of input_tensor_2 is [78 x 3 * 512]

 # Model output
