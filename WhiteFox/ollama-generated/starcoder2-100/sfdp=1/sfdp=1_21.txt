
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        vq = torch.matmul(query1, key2.transpose(-2, -1))  # Compute the dot product of two tensors
        vs  = vq.div(inv_scale_factor)  # Scale the dot product by an inverse scale factor
        softmax_vs  = vs.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_vs  = torch.nn.functional.dropout(softmax_vs, p=dropout_p) # Apply dropout to the softmax output
        vo = dropout_vs.matmul(value2)  # Compute the dot product of the dropout output and a value tensor
        return vo


# Initializing model
m = Model()

# Input tensors for the model
q1 = torch.randn(4, 50, 768)
k2 = torch.randn(50, 937, 768)
v2 = torch.randn(937, 512)

 # Initializing module inputs using input tensors from previous models. It is necessary that the initial model is different from both previous ones. If these three modules were initially identical then you need to generate new input tensors for the current model before initializing them as follows:

q_1 = torch.randn(4, 50, 768) + 3
k_2 = torch.randn(50, 937, 768) * 10
v_2 = torch.randn(937, 512).sigmoid()

 # Initializing the model with the input tensors generated above:
m(q_1, k_2, v_2)

 