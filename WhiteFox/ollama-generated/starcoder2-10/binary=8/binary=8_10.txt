
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other 
        return v1
# Initializing the model and passing in an additional input tensor to be added with the convolutional output.
other_input = torch.randn([32])
m  = Model(other=other_input)

