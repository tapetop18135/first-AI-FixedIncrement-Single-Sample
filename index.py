#########################################################################
#																		#
#	KMUTNB King Mongkut's University of Technology North Bangkok		#
#	Name : Nuttakit Kutparb 580102610032								#
#	Content : Artificial Intelligence use FixPerceptron 				#
#																		#
#########################################################################


import numpy as np
class FixPerseptron:

	def __init__(self,input,target,weight):
		self.input_all = input_all
		self.target = target
		self.weight = np.array(weight)
		self.creatInput_Xall()

	def creatInput_Xall(self):
		for i in range(len(self.input_all)):
			self.input_all[i] = [-1] + self.input_all[i]

		self.input_X_all =  np.array(self.input_all)

	def FixAlgorithm(self):
		i = 0
		check = 0
		interation = 0

		while True:

			interation += 1
			print("interation is : ",interation)
			# select target each sample
			if(self.input_X_all[i][1] == 0 and self.input_X_all[i][2] == 0):
				use_target = self.target[0]
			else:
				use_target = self.target[1]


			# check Err
			if(self.fixcheckErr(self.weight,use_target,self.input_X_all[i])):
				i += 1
				check += 1
				#check if all sample is true return weight
				if(check == len(self.input_X_all)):
					print("success weight is ",self.weight)
					return self.weight

			# else update Weight 
			else:
				self.fixupdateWeight(self.weight,use_target,self.input_X_all[i])
				i += 1 
				check = 0

		# return sample again
			if(i == 4):
					i = 0 

	def fixupdateWeight(self,w,d,x):
		# w(n+1) = w(n) + d * x(each sample) 

		new_weight = w+(d*x)
		self.weight = new_weight
		print(w," + (",d," * ",x ,") = ",self.weight)
		
		return  self.weight 


	def fixcheckErr(self,w,d,x):
		# check err = d * w(transpose) * x(each sample)
		# if result > 0 true
		# if result <= 0 false

		result = np.matmul(w,x)*d
		
		print(w," * ",d," * ",x ," = ",result)

		if(result > 0):
			return True
		else:
			return False


########################## End Class #################################### 

# 2 input 1 output
# 				Or gate
#  x1    x2    (x1 and x2)    class
#   0	  0			0			c2
#   0	  1			1			c1
#   1     0			1			c1	
#   1	  1			1	    	c1
#
# 1 output 2 class c2 = -1 , c1 = c1
input_all = [[0,0],
			 [0,1],
			 [1,0],
			 [1,1]]
target = [-1,1]
weight = [0,0,0]


sample = FixPerseptron(input_all,target,weight)
sample.FixAlgorithm()