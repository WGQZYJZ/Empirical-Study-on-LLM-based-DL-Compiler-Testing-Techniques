
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.tensor([2.5])
        self.dropout = .1
 
    def forward(self, query, key, value):
        vq  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_vq = vq * scale_factor[0]
        softmax_vq = scaled_vq.softmax(dim=-1)
        dropout_vq = torch.nn.functional.dropout(softmax_vq, p=dropout_p, training=self.training)
        output  = dropout_vq.matmul(value)
        return output

# Initializing the model
m  = Model()

