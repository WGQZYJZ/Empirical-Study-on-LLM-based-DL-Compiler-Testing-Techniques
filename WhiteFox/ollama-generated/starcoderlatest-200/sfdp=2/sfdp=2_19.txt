
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.query = torch.nn.Parameter(config["query_weight"].unsqueeze(-1) * \
                                        config["query_bias"] + \
                                        config["kv_scale"] * config["key_weight"], \
                                      requires_grad=False)
        self.key   = torch.nn.Parameter(config["key_weight"], \
                                      requires_grad=False)

        self.scale_factor  = config["kv_scale"]
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(self.scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=config["dropout_p"]) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model({"query_weight": torch.randn(2048, 512),
           "key_weight"   : torch.randn(512,   2048),
           "kv_scale"     : 2.0,
           "dropout_p"    : 0.1})

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
