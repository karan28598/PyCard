'''Copyright (c) 2017 Karan Agrawal
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.'''
def main():
	number = input('Number: ').replace(' ', '')
	digits = [int(char) for char in number]
	digits = digits[::-1]
	# step 1: double alternating digits
	doubled = []
	for (i, digit) in enumerate(digits):
		if (i + 1) % 2 == 0:
			doubled.append(digit * 2)
		else:
			doubled.append(digit)
	# step 2: take away 9 from all numbers larger than 10
	summed = []
	for num in doubled:
		if num < 10:
			summed.append(num)
		else:
			summed.append(num-9)
# step 3: add all the numbers together and divide
	if sum(summed) % 10 == 0:
		print ('VALID')
	else:
		print ('INVALID')
		
if __name__ == "__main__":
    main()
