
class Model(torch.nn.Module):
    def __init__(self, inv_scale=1000):
        super().__init__()
 
        self.query = torch.nn.Parameter(
            torch.randn([32 * 64, 512]) / sqrt(inv_scale)
        )
        self.key   = torch.nn.Parameter(
            torch.randn([32 * 64, 512]) / sqrt(inv_scale)
        )
        self.value = torch.nn.Parameter(torch.randn(32 * 64, 8))
 
    def forward(self):
        scaled_dot_product  = torch.matmul(
            query, key.transpose(-2,-1) # 32*64 * 512 * 512 * 8
        ) / sqrt(512)
 
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output            = attention_weights.matmul(value)

        return output

# Initializing the model with an inverse scale factor of 0.5
model  = Model()

 # Inputs to the model
query    = torch.randn([32,64,512]) / sqrt(.5)  # 32 * 64 * 512
key      = torch.randn([32,64,512]) / sqrt(.5)  # 32 * 64 * 512
value    = torch.randn(32*64,8)                # 32 * 64 * 8

 # Initializing the model with an inverse scale factor of 0.5
model   = Model(.5)

 # Inputs to the model 
 query    = torch.randn([192, 64]) / sqrt(.5)       # 32* 64 * 512
 key      = torch.randn([8, 512], dtype=query.dtype)   # 1024
 value    = torch.randn(1024, 8)                    # 1024 * 8

 # Initializing the model with an inverse scale factor of .7 
 model   = Model(.7)

 # Inputs to the model
 query  = torch.randn([50,32]) / sqrt(2.)          # 32*64 * 512
 key    = torch.randn([8,512], dtype=query.dtype)/sqrt(2)   # 1024 
 value  = torch.randn(1024,8)* 7./9.               # 1024*8

 