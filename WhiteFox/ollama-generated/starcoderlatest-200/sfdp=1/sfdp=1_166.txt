
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm_q = torch.nn.LayerNorm(1024)
 
    def forward(self, qk, key, value, inv_scale_factor):
        qk  = self.layer_norm_q(qk)
 
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(value)
 
        return qk


# Initializing the model
m = Model()

# Query, key, and value tensors to be multiplied with the same model in order to compute the attention weights for each layer of the Transformer decoder network
qk = torch.randn(16, 512, 14, 14)
key = torch.randn(16, 512, 7, 7)
value = torch.randn(16, 3, 14, 14)
inv_scale_factor = 0.1
