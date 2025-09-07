
class Model(torch.nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 5, stride=2)
        self.fc1 = torch.nn.Linear(64 * 7 * 7, d_model)
        self.dropout = torch.nn.Dropout(p=0.25)
 
    def forward(self, x):
        batchsize = x.shape[0]
        # Use `view` to create a shaped tensor:
        # bsz x c x w x h
        x = x.view(batchsize, -1, 7, 7)

        # 32 * 64 * 5 * 5
        x = self.conv1(x)
        # Flatten the input to a 7D tensor:
        # bsz x c x w x h x channels
        x = x.view(batchsize, -1, 7 * 7)

        # Use `Linear` to add a learnable bias to each channel in the 7x7
        # convolution output, and squash with tanh:
        # bsz x d_model
        x = self.fc1(x)
        x = torch.tanh(x)

        return x


# Initializing the model
m = Model(64)

# Inputs to the model
x = torch.randn(2, 3, 7, 7)
