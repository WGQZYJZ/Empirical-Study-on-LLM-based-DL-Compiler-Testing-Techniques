
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        conv = torch.nn.functional.conv2d(x1, self.linear.weight, bias=None, stride=(1, 1), padding=(0, 0)) # Only the batch size is equal to 1 when using convolution function
        bn   = torch.nn.functional.batch_norm(conv)

        output = torch.nn.functional.relu(bn + x2)  # Relu activation follows batch norm
        return self.softmax(bn)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4, 5).to("cuda")
x2 = torch.randn(1, 2, 3, 4).to("cuda")
x3 = torch.randn(1, 1, 3, 4).to("cuda")
