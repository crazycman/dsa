import React, { useState } from 'react'
import { Button, Form, Input } from 'semantic-ui-react'

export const OrganizationFrom = ({onNewOrg}) => {
    const [name, setName] = useState('');

    return (
        <Form>
            <Form.Field>
                <Input 
                    palaceholder="Name der Organization" 
                    value={name} 
                    onChange={e => setName(e.target.value)} />
            </Form.Field>
            <Button onClick={async () => { 
                const org = {name};
                const response = await fetch('/add_org', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(org)
                })
                if (response.ok) {
                    console.log('response ok!');
                    onNewOrg(org);
                    setName('')
                }
            }}>
                Submit
            </Button>
        </Form>
    )
}