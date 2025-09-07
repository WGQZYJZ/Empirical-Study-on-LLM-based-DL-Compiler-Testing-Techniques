
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        scaled_dot_product  = torch.matmul(input1, input2) / np.sqrt(3072) 
        attention_weights  = scaled_dot_product.softmax(dim=-1) # Scaled Dot-Product Attention
        output   = attention_weights * inv_scale
        return v6, v4


# Initializing the model with initial inputs (which will be fixed for future evaluations). Also note that the shapes of the input tensors have been defined as 32 by 3072.
m = Model()
input1   = torch.randn(32, 3072)
input2   = torch.randn(32, 3072)


# Inputs to the model with fixed shape (will be used in future evaluations):
__output__, __output2__  = m(input1, input2)


