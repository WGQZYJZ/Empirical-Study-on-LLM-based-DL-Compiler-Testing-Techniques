
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = v2 .softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        __output__  = dropout_qk.matmul(value)


# Initializing the model
m  = Model()
 
# Input tensors for the model (query and key)
input1  = torch.randn(1024,  65536)
input2  = torch.randn(1024,  65536)

 # Inputs to the model, which are a pair of query tensor and a key tensor
inputs_list = [input1, input2]
 
# The output of the model is the dot product between inputs tensors' last dimension and value tensor. 
outputs = m(inputs_list[0], inputs_list[1])

 