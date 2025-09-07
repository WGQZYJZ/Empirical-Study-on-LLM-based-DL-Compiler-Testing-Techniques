
class Model(torch.nn.Module):
    def __init__(self, dropout=0., inv_scale_factor=1.0):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout)  # Apply dropout to the input tensor
 
        self.linear1 = torch.nn.Linear(256, 49 * 8)
        self.softmax1 = torch.nn.Softmax(dim=-1)  # Apply softmax to the output of the convolutional layer
        self.conv_block1 = torch.nn.Sequential(*[torch.nn.Conv2d(3, 64, 3)] * 2 + [torch.nn.BatchNorm2d(64)])
        self.linear2 = torch.nn.Linear(257 * 8 - 100, 1)
 
        self.activation_fn = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv_block1(x)
        v1 = v1.flatten(-4, -3).permute([2, 0, 1]).contiguous().view([-1] + list(v1.size()[2:]))
        v1 = torch.nn.functional.relu(self.linear1(v1))
 
        # Apply dropout to the output of the convolutional layer 
        v1_softmaxed  = self.activation_fn(self.dropout(torch.reshape(self.softmax1(v1), [-1] + list(x.size()[2:]))))
        return self.linear2(v1).flatten(-3)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(4, 3, 576, 576) + m(x)[0] * m(x)[-1]
__output__  = m(x).view([-1] + list(m(x).size()[-3:]))

