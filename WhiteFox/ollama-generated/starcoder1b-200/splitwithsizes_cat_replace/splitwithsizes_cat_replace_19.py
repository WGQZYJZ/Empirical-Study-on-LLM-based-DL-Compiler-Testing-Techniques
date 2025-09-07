
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, [0], dim=-1) # Split the input tensor along dimensions -1
        concat_list = []
        for i in range(len(v2)):
            c_i = v2[i]  # Extract and save the output of the split operation with respect to dimension `i`
            concat_list.append(c_i)
 
        return torch.cat(concat_list, dim=-1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
