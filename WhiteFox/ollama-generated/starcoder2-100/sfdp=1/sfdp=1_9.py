
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale  = torch.tensor([1 / math.sqrt(2048)]) # The value used in the Transformer model
        v_qk  = torch.matmul(query, key.transpose(-2, -1)) 
        v_qk /= scale
        v_softmax  = nnf.adaptive_max_pool2d(v_qk)
        v_dropout  = dropout(v_softmax)
        output  = v_dropout.matmul(value) 
        return output


# Initializing the model
m = Model()

