
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initialization of the model
m = Model()


# Generate a valid input tensor for the newly generated model.
x1 = torch.randn(8, 64, 32, 32).cuda().half()
query = x1.new_full((64,), float('inf')).cuda()
key = x1.new_full((8, 64), -float('inf')).cuda()
value = x1.new_full((8, 64), float('inf')).cuda()
scale_factor = torch.FloatTensor([5e-3]).cuda().half()
dropout_p = 0.9
