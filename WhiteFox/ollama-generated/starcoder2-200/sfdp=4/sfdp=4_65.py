
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, attn_mask=None):
        qk = torch.einsum('...jq, ...qj -> ...q', query1, key1) / math.sqrt(query1.size(-2)) # Compute the dot product of the query and key
        if not attn_mask is None:
            qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-2)   # Apply softmax to the result
        output = torch.einsum('...q, ...qv -> ...vq', attn_weight, value1).contiguous() # Compute the dot product of the attention weights and the value tensor 
        return output


# Initializing the model
am  = AttentionModel()

# Input tensors for each layer in the transformer block (query, key and values)
q1 = torch.randn(2408, 768)
k1 = torch.randn(539876, 768)
v1 = torch.randn(539876, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q2 = torch.randn(4096, 768)
k2 = torch.randn(3383910, 768)
v2 = torch.randn(3383910, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q3 = torch.randn(405429, 768)
k3 = torch.randn(7944542, 768)
v3 = torch.randn(7944542, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q4 = torch.randn(1000, 768)
k4 = torch.randn(9903104, 768)
v4 = torch.randn(9903104, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q5 = torch.randn(2000, 768)
k5 = torch.randn(3107977, 768)
v5 = torch.randn(3107977, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q6 = torch.randn(2408, 768)
k6 = torch.randn(7159522, 768)
v6 = torch.randn(7159522, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q7 = torch.randn(3074354, 768)
k7 = torch.randn(2000, 768)
v7 = torch.randn(2000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q8 = torch.randn(4593172, 768)
k8 = torch.randn(2048008, 768)
v8 = torch.randn(2048008, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q9 = torch.randn(1357431, 768)
k9 = torch.randn(1357424, 768)
v9 = torch.randn(1357424, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q10 = torch.randn(20000, 768)
k10 = torch.randn(24981435, 768)
v10 = torch.randn(24981435, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q11 = torch.randn(192, 768)
k11 = torch.randn(53081000, 768)
v11 = torch.randn(53081000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q12 = torch.randn(9481320, 768)
k12 = torch.randn(1750000, 768)
v12 = torch.randn(1750000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q13 = torch.randn(9481320, 768)
k13 = torch.randn(9979549, 768)
v13 = torch.randn(9979549, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q14 = torch.randn(2091330, 768)
k14 = torch.randn(10000, 768)
v14 = torch.randn(10000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q15 = torch.randn(2093150, 768)
k15 = torch.randn(4204930, 768)
v15 = torch.randn(4204930, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q16 = torch.randn(13359040, 768)
k16 = torch.randn(5520000, 768)
v16 = torch.randn(5520000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q17 = torch.randn(4390470, 768)
k17 = torch.randn(7500000, 768)
v17 = torch.randn(7500000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q18 = torch.randn(39241830, 768)
k18 = torch.randn(3500000, 768)
v18 = torch.randn(3500000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q19 = torch.randn(2408, 768)
k19 = torch.randn(3579761, 768)
v19 = torch.randn(3579761, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q20 = torch.randn(4000, 768)
k20 = torch.randn(4000, 768)
v20 = torch.randn(4000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q21 = torch.randn(539876, 768)
k21 = torch.randn(539876, 768)
v21 = torch.randn(539876, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q22 = torch.randn(405429, 768)
k22 = torch.randn(405429, 768)
v22 = torch.randn(405429, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q23 = torch.randn(17577800, 768)
k23 = torch.randn(53294775, 768)
v23 = torch.randn(53294775, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q24 = torch.randn(100000, 768)
k24 = torch.randn(5427300, 768)
v24 = torch.randn(5427300, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q25 = torch.randn(1090320, 768)
k25 = torch.randn(799040, 768)
v25 = torch.randn(799040, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q26 = torch.randn(3001420, 768)
k26 = torch.randn(5300000, 768)
v26 = torch.randn(5300000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q27 = torch.randn(194920, 768)
k27 = torch.randn(980000, 768)
v27 = torch.randn(980000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q28 = torch.randn(1435040, 768)
k28 = torch.randn(8442892, 768)
v28 = torch.randn(8442892, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q29 = torch.randn(3001420, 768)
k29 = torch.randn(5300000, 768)
v29 = torch.randn(5300000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q30 = torch.randn(1435040, 768)
k30 = torch.randn(9225000, 768)
v30 = torch.randn(9225000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q31 = torch.randn(434585, 768)
k31 = torch.randn(7045095, 768)
v31 = torch.randn(7045095, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q32 = torch.randn(70394880, 768)
k32 = torch.randn(118400000, 768)
v32 = torch.randn(118400000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q33 = torch.randn(97511040, 768)
k33 = torch.randn(23000000, 768)
v33 = torch.randn(23000000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q34 = torch.randn(19500797, 768)
k34 = torch.randn(4825000, 768)
v34 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q35 = torch.randn(19500797, 768)
k35 = torch.randn(4825000, 768)
v35 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q36 = torch.randn(19500797, 768)
k36 = torch.randn(4825000, 768)
v36 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q37 = torch.randn(19500797, 768)
k37 = torch.randn(4825000, 768)
v37 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q38 = torch.randn(19500797, 768)
k38 = torch.randn(4825000, 768)
v38 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q39 = torch.randn(19500797, 768)
k39 = torch.randn(4825000, 768)
v39 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q40 = torch.randn(19500797, 768)
k40 = torch.randn(4825000, 768)
v40 = torch.randn(4825000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q41 = torch.randn(9308940, 768)
k41 = torch.randn(28200000, 768)
v41 = torch.randn(28200000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q42 = torch.randn(93579920, 768)
k42 = torch.randn(172800000, 768)
v42 = torch.randn(172800000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q43 = torch.randn(95032720, 768)
k43 = torch.randn(141000000, 768)
v43 = torch.randn(141000000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q44 = torch.randn(29517000, 768)
k44 = torch.randn(30000000, 768)
v44 = torch.randn(30000000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q45 = torch.randn(29517000, 768)
k45 = torch.randn(30000000, 768)
v45 = torch.randn(30000000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q46 = torch.randn(29517000, 768)
k46 = torch.randn(30000000, 768)
v46 = torch.randn(30000000, 768)

 # Input tensors for each layer in the transformer block (query, key and values)
q47 = torch.randn(29517000, 768)
k47 = torch.randn(30000000, 768)
v47 = torch.