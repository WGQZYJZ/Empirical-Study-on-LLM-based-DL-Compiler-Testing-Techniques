class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model<|end_of_model|>m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # This should be different from the previous model inputs.
