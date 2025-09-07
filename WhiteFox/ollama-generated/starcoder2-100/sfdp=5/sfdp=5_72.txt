
class AttentionModel(torch.nn.Module):
    def __init__(self, dmodel=512, nhead=8):
        super().__init__()

        self.dmodel = dmodel  # Set the dimension of the model to be 512
        self.nhead = nhead   # Set the number of heads to 8

        self.attn = torch.nn.MultiheadAttention(
            d_model=self.dmodel, 
            num_heads=self.nhead)

    def forward(self, query, key, value):
        qk  = self.attn(query, key)[0]
        attn_weight  = torch.softmax(qk, dim=-1) 
        attn_weight  = torch.dropout(attn_weight, dropout_p=0.5, is_training=True) 
        output  = attn_weight @ value 
        return output


# Initializing the model
model  = AttentionModel()

 # Inputs to the model
        __inputs__ = torch.randn([16, 512])
        self._query  = __inputs__.clone().detach_()  
        self._key  = __inputs__.clone().detach_() 
        self._value  = __inputs__.clone().detach_() 


# ## Model

# class TransformerBlock(torch.nn.Module):
    
#     def forward(self, inputs1) :
#         # 2 - Multi Head Attention  
#         att_outputs  = multi_head_attention_layer(
#             key=inputs1 , 
#             query=inputs1, 
#             value=inputs1 )
        
  # 5 - Residual Connection + Layer Norm
   # layernorm1  = torch.nn.LayerNorm()
       
#     #  6 - Positionwise FeedForward Network
#     ff_out = feedforward_network(att_outputs)
    
#     model_output = torch.add(inputs , ff_out ) # Residual Connection
        
  # 7 - LayerNorm  
#     return layernorm1(model_output)

# m  = TransformerBlock()


# Input to the model
x1 = torch.randn([8,50,32])
