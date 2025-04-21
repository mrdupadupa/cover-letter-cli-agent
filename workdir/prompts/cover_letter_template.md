
# COVER LETTER GENERATION TASK

## INPUT DATA

- Position: {position}
- Company: {company_name}
- Requirements: {requirements}
- Candidate Experience: {years_experience} years in {field}
- Candidate Skills: {skills}
- Candidate Name: {candidate_name}
- Candidate Email: {candidate_email}
- Candidate Phone: {candidate_phone}
- Candidate Address: {candidate_address}
- Date: {date}
- Max Length: {max_length} words

## OUTPUT FORMAT

Generate a markdown-formatted cover letter with:

1. Header section with candidate contact information
2. Professional greeting
3. 3-4 paragraphs addressing requirements and highlighting skills
4. Professional closing with candidate name
5. No placeholder text - all fields should be filled with actual content

## CONTENT REQUIREMENTS

- Address specific job requirements directly
- Highlight relevant candidate experience and skills
- Show knowledge of {company_name}'s business domain
- Use professional but conversational language
- Avoid generic phrases and clichés
- Sound human-written, not AI-generated
- Stay under {max_length} words total

## FORMATTING INSTRUCTIONS

1. Use Markdown for formatting
2. Use bullet points, and **bold text** where appropriate
3. Don't make sections in the text
4. Include a contact information block with the {candidate_name}, {candidate_email}, {candidate_phone}, {candidate_address} in the beginning in the left top corner of the document before the greeting or body of the letter. Every contact option should be from the new line.  Use HTML tags to style the block if PDF conversion supports it (e.g., Pandoc). Ensure:Font size is set to 10pt Text is left-aligned.Line spacing is clear and readable (line-height: 1.4).Only the name is bolded for visual hierarchy.Emojis help visually highlight contact types; they can be removed for more formal styles.
5. Use a professional greeting like "Dear Hiring Manager,"
6. No futter!
7. Use a professional closing like "Sincerely,"
8. Put {candidate_name} in the end after "Sincerely"
9. Add an empty line after the candidate name
10. Place the date (`{date}`) on a new line immediately after the closing signature ("Sincerely," and the candidate name) at the end of the letter
11. Use a professional font and size
12. Is no longer than {max_length} words

Save the cover letter in a file named {company_name}_cover_letter.md in /workspace directory.