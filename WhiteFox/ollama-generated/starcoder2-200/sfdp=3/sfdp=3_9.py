
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1, qk2): # two input tensors are needed
        v1  = torch.matmul(qk1, qk2.transpose(-2, -1)) 
        scaled_qk = v1 * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = softmax_qk
        output  = dropout_qk .matmul(qk2) # This line needs to be modified
        return output


# Initializing the model
m = Model()


# Inputs to the model