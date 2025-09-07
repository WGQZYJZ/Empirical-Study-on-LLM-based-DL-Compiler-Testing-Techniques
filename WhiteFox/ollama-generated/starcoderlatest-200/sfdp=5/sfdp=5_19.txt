
class Model(torch.nn.Module):
    def __init__(self, dim_in=768, dim_hidden=3072, dim_out=1024):
        super().__init__()
        self.conv = torch.nn.Conv2d(dim_in, dim_hidden, kernel_size=1)
        self.fc  = torch.nn.Linear(dim_hidden, dim_out)
 
    def forward(self, x):
        x  = F.dropout(F.relu(self.conv(x)), p=0.5) # Apply dropout before the convolutional layer
        output = F.softmax(self.fc(x), dim=-1)    # Apply softmax on the output from the last convolutional layer
        return output


# Initializing the model
m = Model()

# Inputs to the model
__query__  = torch.randn(1, 3, 64, 64)
__key__   = torch.randn(1, 128, 64, 64)
__value__ = torch.randn(1, 512, 64, 64)
__attn_mask__ = torch.zeros(__query__.size())
output      = m(__query__, __key__, __value__)


