
class AttentionModel(torch.nn.Module):
    def __init__(self, num_head=2, dmodel=8, nblocks=4):
        super().__init__()
        self.num_head = num_head
        self.dmodel = dmodel
 
        self.attn1  = torch.nn.Linear(3 * dmodel // num_head, 5 * dmodel) # Linear layer of input size 3 * dmodel / num_head to output size 5 * dmodel
        self.attn2  = torch.nn.Linear(3 * dmodel // num_head, 7 * dmodel) # Linear layer of input size 3 * dmodel / num_head to output size 7 * dmodel
 
        self.res_attn1 = torch.nn.Dropout(0.5) # Dropout layer with dropout probability 0.5
        self.res_attn2 = torch.nn.Dropout(0.5) # Dropout layer with dropout probability 0.5
 
        self.norm1 = torch.nn.LayerNorm(dmodel) 
        self.norm2 = torch.nn.LayerNorm(dmodel)
 
        self.block1 = torch.nn.TransformerEncoderLayer(dmodel, nheads=num_head, dim_feedforward=3 * dmodel // num_head + 5) # The transformer encoder layer with 3 * dmodel / num_head inputs, the rest as usual
        self.block2 = torch.nn.TransformerEncoderLayer(dmodel, nheads=num_head, dim_feedforward=3 * dmodel // num_head + 7)
 
        self.lastnorm1 = torch.nn.LayerNorm(dmodel) 
        self.lastnorm2 = torch.nn.LayerNorm(dmodel)
        self.lastout  = torch.nn.Linear(5, 4) # The output of the network is a fully connected layer with input size 5 and output size 4
 
        self.relu  = torch.nn.ReLU() 
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, input):
        q1 = self.attn1(input) # Compute the dot product of the query and key
        k1 = q1 @ q1.transpose(-2, -1) / math.sqrt(q1.size(-1))  # Compute the dot product of the scaled query with the transposed key
        msk_q1 = torch.triu(torch.ones((input.shape[0], input.shape[-2], input.shape[-1]), dtype=torch.bool), diagonal=1) 
        k1 = torch.masked_fill_(k1,  msk_q1, -9e8) # Fill the masked part of this matrix with very large negative numbers
        k1 += torch.tril(torch.ones((input.shape[0], input.shape[-2], input.shape[-1]), dtype=torch.bool), diagonal=-1).to(k1.dtype) 
        attn_w1 = torch.softmax(k1, dim=-1) # Apply softmax to the result
        attn_w1  = self.res_attn1(attn_w1 * input)
 
        q2 = self.attn2(input)  
        k2 = q2 @ q2.transpose(-2, -1) / math.sqrt(q2.size(-1)) 
        msk_q2 = torch.triu(torch.ones((input.shape[0], input.shape[-2], input.shape[-1]), dtype=torch.bool), diagonal=1)  
        k2 += torch.masked_fill_(k2,  msk_q2, -9e8) 
        k2 = torch.masked_fill_(k2 + attn_w1 * q2, torch.tril(torch.ones((input.shape[0], input.shape[-2], input.shape[-1]), dtype=torch.bool), diagonal=-1).to(k2.dtype), -9e8) 
        attn_w2 = torch.softmax(k2, dim=-1)  
        attn_w2  = self.res_attn2(attn_w2 * input)
        attn_w3 = (self.block1((attn_w1 @ q1) + attn_w2 @ q2))[0] # Compute the dot product of these attention weights and the query
 
        norm_1 = self.norm1(attn_w1 @ 5 + 5) 
        norm_2 = self.norm2(attn_w2 @ 7 + 4 * k2)
 
        attn_weight,  attn_score  = (self.lastout((norm_1 @ q2 @ q3).argmax(-1)) @ 9)[0] # Compute the dot product of these attention weights and the query
        attn_w3 = self.sigmoid(attn_weight + attn_score) * input  # Apply softmax to the result
        return attn_w3
 
# Inputs to the model
input1,  input2  = torch.randn(400, 5), torch.randn(800, 900, 600, dtype=torch.float32)

