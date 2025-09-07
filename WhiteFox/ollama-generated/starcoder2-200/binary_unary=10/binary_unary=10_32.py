
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = F.linear(x1[0]) # Linear transformation with one parameter: the bias
        v2  = v1 + 0.5 # Add another scalar constant to the output of the linear transformation
        return torch.relu(v2)


m  = Model()
 
 __output__  = m(input_tensors[0], input_tensors[1])
