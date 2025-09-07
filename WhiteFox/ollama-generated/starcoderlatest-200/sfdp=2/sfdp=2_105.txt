
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(768, 3072)
        self.relu = torch.nn.ReLU()
 
        # This line should be deleted before generating the new model
#        self.conv = torch.nn.Conv2d(512, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        x = x.permute((0, 3, 1, 2)) # permute the input tensor to NCHW format
 
        # Add a new dimension for batch size and move it before applying the linear layer
#        x = x.unsqueeze(dim=0)
#        x = x.permute((0, 2, 3, 1))
#        print('x shape', x.shape)
 
        x = self.linear1(x)
        x = torch.transpose(x, -1, -2).contiguous() # permute the output of linear layer to CHW format
        x = self.relu(x)
 
#        x = self.conv(x)

        return x


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
