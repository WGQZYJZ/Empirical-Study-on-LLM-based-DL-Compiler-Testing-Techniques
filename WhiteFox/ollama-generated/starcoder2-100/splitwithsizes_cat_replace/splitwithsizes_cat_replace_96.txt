
class Model(torch.nn.Module):
    def __init__(self, num_channels=32):
        super().__init__()
        self.split  = torch.nn.Conv2d(num_channels, num_channels * 10, kernel_size=(7, 7), stride=[1 for i in range(len(split))], padding=3)
 
    def forward(self, input):
        split_tensors = torch.split(input, self.split.kernel_size[0] * self.split.stride[0], dim=2)
        concatenated  = torch.cat([split_tensors[i] for i in range(len(split))], dim=2) 
        return self.split(concatenated)


# Initializing the model
m  = Model()
 
# Inputs to the model
input  = torch.randn(1, m.split.kernel_size[0] * m.split.stride[0], 64, 64)

 # The return line is not triggered since there are multiple calls of torch.split and torch.cat in the model
 
# Return line without a call to torch.split or torch.cat
m(input) 
return True

