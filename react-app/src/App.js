import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import { Orgnizations } from './components/Organizations';
import { OrganizationFrom } from './components/OrganizationForm';
import { Container } from 'semantic-ui-react';

function App() {
  const [orgs, setOrgs] = useState([]);

  useEffect(() => {
    fetch("/orgs").then(response => 
      response.json().then(data => {
        setOrgs(data.orgs);
      })
    )
  }, []);

  console.log(orgs);
  orgs.map(org => org.members.map(m => console.log(m)));

  return (
    /* <div className="App"> */
      <Container style={{marginTop: 40}}>
        <OrganizationFrom onNewOrg={org => setOrgs(currentOrgs => [org, ...currentOrgs])} />
        <Orgnizations orgs={orgs} />
      </Container>
    /* </div> */
  )
}

export default App;
