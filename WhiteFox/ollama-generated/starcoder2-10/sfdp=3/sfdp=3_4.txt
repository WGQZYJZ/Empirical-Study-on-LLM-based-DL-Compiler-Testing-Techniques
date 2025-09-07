
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(0.7)
        self.dropout_p = torch.nn.Parameter(0.1)
 
    def forward(self, query, key, value):
        scale_factor  = self.scale ** -2
        vq = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_vq  = vq.mul(scale_factor)
        softmax_vq = scaled_vq.softmax(dim=-1)
        dropout_vq = torch.nn.functional.dropout(softmax_vq, p=self.dropout_p)
        return dropout_vq.matmul(value)


# Initializing the model
m  = Model()
scale_factor  = m.scale**-2 # Set the scale factor to 0.7. This parameter is an internal parameter of the model and should not be externally tuned or modified by the user.


# Inputs to the model: 10 queries, 3 keys and 4 values tensors with the same size (6x5)
queries = torch.rand(2, 10, 5)
keys    = torch.rand(2, 10, 5) # These tensors are used as inputs to compute the dot product of a query and key tensor. They have the same size.
values  = [torch.rand(2, 6, 5)] * 4


# Executing the model: pass in multiple input tensors. The user does not need to provide all four input tensors at once; they can pass in one of them and it will be automatically replicated into the other three inputs
for k in values[:-1]:
    print(m(queries, keys, [k] + list(values[0:])))

