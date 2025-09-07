
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        conv  = torch.nn.functional.conv2d(...) # X should be a channel dimension or an index representing the number of channels in input_tensor
        bn    = torch.nn.functional.batch_norm(...) # If the output of this module has more than 2 dimensions, then X should match with that dimension 
        output = bn(conv(x1))
        return output


# Initializing the model
m = Model()


