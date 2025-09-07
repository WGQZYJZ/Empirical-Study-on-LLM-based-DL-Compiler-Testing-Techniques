
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2, -1))
        v2  = v1 / inv_scale_factor
        v4  = torch.nn.functional.dropout(torch.softmax(v2, dim=-1), p=dropout_p) 
        return v4 .matmul(value3)


# Initializing the model
m  = Model() 

# Input to the model
query1  = torch.randn(640, 768).to(device)
key2   = torch.randn(512, 768).to(device)
value3 = torch.randn(512, 768).to(device)

 # Generate valid inputs to the model
inv_scale_factor  = np.random.rand() + (np.random.choice([0.04]))  ## a fixed float constant 
dropout_p         = np.random.rand() * 3 

# Input tensors to the model
__query1__      = torch.randn(640, 768).to(device)  # randomly generated input tensor with shape (640, 768) and type float32 on the GPU device 
__key2__        = torch.randn(512, 768).to(device)  # randomly generated input tensor with shape (512, 768) and type float32 on the GPU device
__value3__      = torch.randn(512, 768).to(device)  # randomly generated input tensor with shape (512, 768) and type float32 on the GPU device

__output__        = m(__query1__, __key2__, __value3__)