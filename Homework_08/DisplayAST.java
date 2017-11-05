/******************************************************************************
Program:		A class for viewing a Parse-Tree for JJT Parser
			
Date:			11/04/2017
Written by: 	Ankit Manerikar
Project:		ECE 664 - Homework 8
Reference: 
https://engineering.purdue.edu/kak/DesigningWithObjects/dwocode/chap16/chap16.html
******************************************************************************/


public class DisplayAST {

    private int branchnum = 0;
 
 	/*Generate branches for the parse tree*/
    private String dispbranch() {
        String branchstring = "      ";
        for (int i=0;  i< branchnum; i++ ) {
            
            branchstring += "      ";
            if(i==branchnum-1){
            branchstring += "`-->";
            }
        }
        return branchstring;
    }

	/*Recursive Function to search all nodes for parse-tree generation*/
    public void viewParseTree(Node CurrToken) {
        System.out.println( dispbranch() + CurrToken.toString());
        
        ++branchnum;
        int count = CurrToken.jjtGetNumChildren();
        for (int i=0;i<CurrToken.jjtGetNumChildren();i++) {
            Node ChildNode = CurrToken.jjtGetChild(i);
            viewParseTree(ChildNode);
        }
        --branchnum;	  
    }
}

/******************************************************************************/

