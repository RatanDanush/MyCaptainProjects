{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[]\n",
    "a=input(\"Enter numbers seperated by space:\")\n",
    "odd=[]\n",
    "even=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in a:\n",
    "    if i%2==0:\n",
    "        even.append(i)\n",
    "    else:\n",
    "        odd.append(i)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5]\n",
      "[2, 4]\n"
     ]
    }
   ],
   "source": [
    "print(\"ODD:{}\".format(odd))\n",
    "print(\"EVEN:{}\".format(even))"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "##tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n"
     ]
    }
   ],
   "source": [
    "tup=('Hi','Bye')\n",
    "if len(a)%2==0:\n",
    "    print(tup[0])\n",
    "else:\n",
    "    print(tup[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BEFORE:{1: 'ONE', 2: 'TWO', 3: 'THREE'}\n",
      "AFTER:{2: 'TWO', 3: 'THREE'}\n"
     ]
    }
   ],
   "source": [
    "dictionary={1:\"ONE\",2:\"TWO\",3:\"THREE\"}\n",
    "print(\"BEFORE:{}\".format(dictionary))\n",
    "dictionary.pop(1)\n",
    "print(\"AFTER:{}\".format(dictionary))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
