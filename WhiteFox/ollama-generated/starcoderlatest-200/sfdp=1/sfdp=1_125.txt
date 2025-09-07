
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value, attention_mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 3, 64, 64) # [batch_size, head, length, dimension]
key    = torch.randn(1, 8,  64, 64) # [batch_size, head, sequence_length, dimension]
value  = torch.randn(1, 8,  64, 64) # [batch_size, head, sequence_length, dimension]


# Output of the model on random inputs
output = m(query, key, value, attention_mask=None)


